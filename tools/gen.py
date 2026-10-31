import json,re,collections,hashlib
days=json.load(open('/tmp/raw.json'))
DOW={'Sunday':0,'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6}
def j(x): return re.sub(r'\s+',' ',(x or '')).strip()
issues=[]
def issue(day,msg): issues.append('W%d %s (Day %d): %s'%(day['week'],day['dow'],day['day'],msg))
MUSMAP=[(r'chest|pec','Chest'),(r'back|lat|trap|rhomboid','Back'),(r'shoulder|delt','Shoulders'),(r'bicep|tricep|forearm|brachial|arm','Arms'),(r'abs|core|oblique','Core'),(r'glute','Glutes'),(r'quad|hamstring|calf|calves|leg|hip|adductor|abductor','Legs')]
def mus(p):
    for rx,m in MUSMAP:
        if re.search(rx,p,re.I): return m
    return 'Full body'
EXD={}; exkey={}
def exd_key(name,prim,sec,diff,instr,br,alt):
    base=re.sub(r'[^a-z0-9]+','-',name.lower()).strip('-')
    val=dict(p=prim,s=sec,d=diff,i=instr,b=br,a=alt)
    k=base
    n=1
    while k in EXD and EXD[k]!=val:
        n+=1;k=base+'-v%d'%n
    EXD[k]=val
    return k
def reps_tok(t,day):
    """returns reps,secs,rt for a reps token like '10-12','12/side','30 s','max reps'"""
    t=j(t)
    side=re.search(r'/(side|leg|arm|hand)$',t)
    suf=('/'+side.group(1)) if side else ''
    core=t[:-len(suf)] if suf else t
    m=re.match(r'^(\d+)\s*s$',core)
    if m: return 0,int(m.group(1)),'%s sec%s'%(m.group(1),suf)
    if re.match(r'^\d+(-\d+)?$',core):
        top=int(core.split('-')[-1]); return top,0,'%s%s'%(core,suf) if suf else core+' reps'
    if core=='max reps': return 0,0,'max reps'+suf
    if core=='max s': return 0,0,'max hold (seconds)'+suf
    issue(day,'unrecognised reps token %r'%t); return 0,0,t
def parse_ex_cell(c):
    lines=[l for l in (c or '').split('\n')]
    idx=next(i for i,l in enumerate(lines) if l.startswith('Primary:'))
    name=j(' '.join(lines[:idx])); lab=''
    m=re.match(r'^(Stage \d|[A-D]) (.+)$',name)
    if m: lab,name=m.group(1),j(m.group(2))
    rest=j(' '.join(lines[idx:]))
    parts=re.split(r'(Primary|Secondary|Weight|Difficulty): ',rest)
    f={parts[i]:j(parts[i+1]) for i in range(1,len(parts)-1,2)}
    return lab,name,f
def parse_desc(c):
    t=j(c)
    m=re.match(r'^(.*?)(?: Breathing: (.*?))?(?: Alternative: (.*))?$',t)
    return m.group(1) or '',m.group(2) or '',m.group(3) or ''
def dur_secs(t):
    m=re.search(r'(\d+(?:\.\d+)?)\s*min',t)
    if m: return int(round(float(m.group(1))*60))
    m=re.search(r'(\d+)\s*s\b',t)
    return int(m.group(1)) if m else 0
def norm_per(t):
    t=re.sub(r'(\d+) per side',r'\1/side',t); t=re.sub(r'(\d+) per leg',r'\1/leg',t); return t
plan={}; guide=[]
stats=collections.OrderedDict()
for d in days:
    w=d['week']; dow=DOW[d['dow']]
    info=list(d['info']); title=''
    first=info[0] if info else ''
    mt=re.match(r'^(.*?) Intensity',first)
    title=j(mt.group(1)) if mt else j(first)
    pre=[];main=[];post=[];br_before=[];br_after=[];cardio=[];yoga=[];notes=[]
    st=dict(pre=0,blocks=0,main=0,post=0,br=0,cardio=0,yoga=0)
    for sk in d['order']:
        S=d['sections'][sk]
        for nline in S['notes']: notes.append(S['title']+': '+nline if False else nline)
        for t in S['tables']:
            if t['type']=='pre':
                for r in t['rows']:
                    tp,n,du,tm=[j(x) for x in r]
                    du2=norm_per(du); secs=dur_secs(du2) if re.search(r'\d\s*(min|s)\b',du2) and not re.search(r'per minute',du2.split(',')[0]) else 0
                    mm=re.match(r'^(\d+(?:\.\d+)?) min',du2)
                    if mm: secs=int(float(mm.group(1))*60)
                    elif re.match(r'^\d+ s\b',du2): secs=int(re.match(r'^(\d+) s',du2).group(1))
                    else: secs=0
                    reps=0
                    if not secs:
                        mr=re.match(r'^(\d+)',du2); reps=int(mr.group(1)) if mr else 0
                        if not mr: issue(d,'warm-up duration not parsed: '+du)
                    rt=du2
                    e=dict(n=n,m='Warm-up',c='pre',sets=1,reps=reps,secs=secs,rt=rt,tp=tp,est=tm,load='')
                    pre.append(e);st['pre']+=1
            elif t['type']=='block':
                hdr=t['header']; H=j(hdr)
                mk=re.match(r'^Block (\d+): (SUPERSET|STRAIGHT SETS|TRI-SET|MECHANICAL DROP SET) \| (.*)$',H)
                if not mk: issue(d,'block header not parsed: '+H[:60]); continue
                bno,kind,spec=int(mk.group(1)),mk.group(2),mk.group(3)
                nsets=int(re.search(r'(\d+) (?:sets|rounds)',spec).group(1))
                restm=re.search(r'then rest (\d+) s',spec) if kind!='STRAIGHT SETS' else re.search(r'Rest between sets: (\d+) s',spec)
                rest=int(restm.group(1)) if restm else None
                if rest is None: issue(d,'rest not found in block %d header'%bno)
                note=j(spec)
                exs=[]
                for r in t['rows']:
                    lab,name,f=parse_ex_cell(r[0]); instr,brt,alt=parse_desc(r[2]); sc=j(r[1])
                    m1=re.match(r'^(\d+) sets x (.+?) Rest between sets: (\d+) s$',sc)
                    m2=re.match(r'^(\d+) rounds?: (.+)$',sc)
                    m3=re.match(r'^(.+?) Sets: (\d+) of the full drop set$',sc)
                    if m1: ns,rtok,rr=int(m1.group(1)),m1.group(2),int(m1.group(3))
                    elif m2: ns,rtok,rr=int(m2.group(1)),m2.group(2),None
                    elif m3: ns,rtok,rr=int(m3.group(2)),m3.group(1),None
                    else: issue(d,'sets cell not parsed: '+sc); continue
                    if ns!=nsets: issue(d,'sets mismatch block %d: header %d vs row %d (%s)'%(bno,nsets,ns,name))
                    if m1 and rr!=rest: issue(d,'rest mismatch block %d'%bno)
                    reps,secs,rt=reps_tok(rtok,d)
                    k=exd_key(name,f.get('Primary',''),f.get('Secondary',''),f.get('Difficulty',''),instr,brt,alt)
                    wt=f.get('Weight','')
                    exs.append(dict(lab=lab,n=name,reps=reps,secs=secs,rt=rt,load=wt,x=k,m=mus(f.get('Primary','')),prim=f.get('Primary','')))
                st['blocks']+=1;st['main']+=len(exs)
                if kind=='STRAIGHT SETS':
                    for e in exs:
                        main.append(dict(n=e['n'],m=e['m'],c='main',sets=nsets,reps=e['reps'],secs=e['secs'],rt=e['rt'],load=e['load'],restS=rest,x=e['x'],bn='Block %d: %s'%(bno,note)))
                else:
                    label={'SUPERSET':'Superset','TRI-SET':'Tri-set','MECHANICAL DROP SET':'Drop set'}[kind]
                    for rd in range(1,nsets+1):
                        for ix,e in enumerate(exs):
                            last=(ix==len(exs)-1)
                            main.append(dict(n=e['n'],m=e['m'],c='main',sets=1,reps=e['reps'],secs=e['secs'],rt=e['rt'],load=e['load'],restAfter=(rest if last else 0),x=e['x'],blk='%s %s, round %d of %d'%(label,e['lab'] or str(ix+1),rd,nsets) if kind!='MECHANICAL DROP SET' else 'Drop set %s, round %d of %d'%(e['lab'] or str(ix+1),rd,nsets),bn='Block %d: %s'%(bno,note)))
            elif t['type']=='post':
                for r in t['rows']:
                    n,tg,du,bt=[j(x) for x in r]
                    m=re.match(r'^(\d+) s hold x (\d+) reps',du); m2=re.match(r'^(\d+) slow reps',du)
                    if m:
                        s_,rp=int(m.group(1)),int(m.group(2))
                        for q in range(1,rp+1):
                            post.append(dict(n=n,m='Cool-down',c='post',sets=1,reps=0,secs=s_,rt='%d sec hold'%s_,tg=tg,bth=bt,blk='hold %d of %d'%(q,rp),dtx=du,load=''));st['post']+=1
                    elif m2:
                        post.append(dict(n=n,m='Cool-down',c='post',sets=1,reps=int(m2.group(1)),secs=0,rt='%s slow reps'%m2.group(1),tg=tg,bth=bt,dtx=du,load=''));st['post']+=1
                    else: issue(d,'stretch duration not parsed: '+du)
            elif t['type']=='br':
                for r in t['rows']:
                    n,when,du,timing,how=[j(x) for x in r]
                    mm=re.match(r'^(\d+) min, (\d+) cycles$',du)
                    tmv=dict(i=0,h=0,o=0,h2=0); toks=[(a.title(),b) for a,b in re.findall(r'(In|Hold|Out) (\d+(?:\.\d+)?) s',timing,re.I)]; hs=0
                    for lab,v in toks:
                        v=int(float(v))
                        if lab=='In': tmv['i']=v
                        elif lab=='Out': tmv['o']=v
                        else:
                            if tmv['o']==0 and tmv['i']>0 and hs==0: tmv['h']=v
                            else: tmv['h2']=v
                            hs+=1
                    if not mm or not toks or not tmv['i'] or not tmv['o']: issue(d,'breathing not parsed: %s | %s'%(du,timing)); continue
                    cyc=int(mm.group(2)); cl=sum(tmv.values()); secs=int(mm.group(1))*60
                    if abs(cyc*cl-secs)>cl: issue(d,'breathing cycles*length (%d) differs from %d s for %s'%(cyc*cl,secs,n))
                    e=dict(n=n,m='Breathing',c='br',sets=1,reps=0,secs=secs,rt=du,tm=tmv,when=when,how=how,tmx=timing,cyc=cyc,load='')
                    (br_before if re.search(r'before',when,re.I) else br_after).append(e);st['br']+=1
            elif t['type'] in('cardio','yoga'):
                for r in t['rows']:
                    if t['type']=='cardio':
                        n,du,g=[j(x) for x in r]; e=dict(n=n,m='Cardio',c='flow',sets=1,reps=0,secs=dur_secs(du),rt=du,cue=g,load='');cardio.append(e);st['cardio']+=1
                    else:
                        n,du,tg,bt=[j(x) for x in r]; e=dict(n=n,m='Yoga',c='flow',sets=1,reps=0,secs=dur_secs(du),rt=du,tg=tg,bth=bt,load='');yoga.append(e);st['yoga']+=1
    sunday=(dow==0)
    if sunday:
        # PDF order: A cardio, B yoga, C breathing (before cardio / after yoga)
        ex=br_before+cardio+yoga+br_after
    else:
        ex=br_before+pre+main+post+br_after+cardio
    if not ex: issue(d,'no exercises')
    plan.setdefault(w,{})[dow]=dict(name=title,ex=ex,info=info+['']+[n for n in notes if n.strip()],day=d['day'],phase=d['phase'])
    stats[d['day']]=dict(week=w,dow=d['dow'],title=title,**st,items=len(ex))
json.dump(dict(plan=plan,exd=EXD,stats=stats,issues=issues),open('/tmp/plan4.json','w'))
print('days',len(stats),'exd',len(EXD),'issues',len(issues))
for i in issues[:25]: print(' -',i)
tot=collections.Counter()
for s in stats.values():
    for k in ('pre','blocks','main','post','br','cardio','yoga','items'): tot[k]+=s[k]
print(dict(tot))
