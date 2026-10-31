import pickle,re,json,collections
ev=[e for e in pickle.load(open('/tmp/ev.pkl','rb')) if e[1]<=133]
NOISE=re.compile(r'^8-Week Progressive Muscle Gain Programme Page \d+$')
def clean(t): return '\n'.join(l for l in t.split('\n') if not NOISE.match(l.strip())).strip()
HDR=re.compile(r'Week (\d) \| (\w+) \(Day (\d+) of 56\)\s*(.*)')
KINDS={('Type','Exercise'):'pre',('Stretch','Target muscle'):'post',('Technique','When'):'br',('Activity','Duration'):'cardio',('Pose / stretch','Time'):'yoga'}
days=[];cur=None;sec=None
def j(x): return re.sub(r'\s+',' ',(x or '')).strip()
for kind,pgno,data in ev:
    if kind=='text':
        t=clean(data)
        if not t: continue
        lines=t.split('\n')
        i=0
        while i<len(lines):
            l=lines[i]
            m=re.match(r'Week (\d) \| (\w+) \(Day (\d+) of 56\)\s*(.*)',l)
            if m:
                cur={'week':int(m.group(1)),'dow':m.group(2),'day':int(m.group(3)),'phase':m.group(4),'info':[],'sections':{}, 'order':[]}
                days.append(cur);sec=None;i+=1;continue
            h=re.match(r'^([A-F])\. (.+)$',l)
            if h and cur:
                sec=h.group(1);cur['sections'][sec]={'title':h.group(2),'notes':[],'tables':[]};cur['order'].append(sec);i+=1;continue
            if cur:
                if sec is None: cur['info'].append(l)
                else: cur['sections'][sec]['notes'].append(l)
            i+=1
    else:
        rows=data
        if not rows or not cur: continue
        h0=j(rows[0][0])
        if h0.startswith('Block'):
            if sec is None or sec not in cur['sections']: raise Exception('block outside section p%d'%pgno)
            cur['sections'][sec]['tables'].append({'type':'block','header':rows[0][0],'rows':rows[1:]})
        else:
            key=(j(rows[0][0]),j(rows[0][1]))
            k=KINDS.get(key)
            if k is None: raise Exception('unknown table %s p%d'%(key,pgno))
            S=cur['sections'][sec]
            if S['tables'] and S['tables'][-1]['type']==k: S['tables'][-1]['rows']+=rows[1:]
            else: S['tables'].append({'type':k,'header':rows[0],'rows':rows[1:]})
json.dump(days,open('/tmp/raw.json','w'),indent=1)
print(len(days),'days')
c=collections.Counter((d['dow']) for d in days); print(c)
bad=[d['day'] for d in days if sorted(d['sections'])==[]]; print('empty days',bad)
secs=collections.Counter((d['dow'] in('Sunday',),tuple(sorted(d['sections']))) for d in days); print(secs)
# unique patterns
reps=collections.Counter(); durs=collections.Counter(); tcols=collections.defaultdict(collections.Counter)
for d in days:
    for k,S in d['sections'].items():
        for t in S['tables']:
            if t['type']=='block':
                for r in t['rows']: reps[j(r[1])]+=1
            else:
                for r in t['rows']:
                    tcols[t['type']][j(r[2] if t['type'] in('pre','br','post') else r[1])]+=1
print('--- block sets cells',len(reps))
for k,v in sorted(reps.items(),key=lambda x:-x[1])[:60]: print(v,repr(k))
