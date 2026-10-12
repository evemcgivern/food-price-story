import json, html
from pathlib import Path
source=Path('data/source/us-states-albers-10m.json')
doc=json.loads(source.read_text())
transform=doc['transform']; sx,sy=transform['scale']; tx,ty=transform['translate']
arcs=[]
for arc in doc['arcs']:
    x=y=0; points=[]
    for dx,dy in arc:
        x+=dx; y+=dy
        points.append((x*sx+tx,y*sy+ty))
    arcs.append(points)
def arc(i):
    points=arcs[i if i>=0 else ~i]
    return points if i>=0 else list(reversed(points))
def rings_for(g):
    result=[]
    polygons=g['arcs'] if g['type']=='MultiPolygon' else [g['arcs']]
    for poly in polygons:
        for ring in poly:
            points=[]
            for idx in ring:
                part=arc(idx)
                points.extend(part if not points else part[1:])
            if points: result.append(points)
    return result
# Census state and district FIPS to Census division.
divisions={
 'New England':{'region':'Northeast','states':['09','23','25','33','44','50']},
 'Middle Atlantic':{'region':'Northeast','states':['34','36','42']},
 'East North Central':{'region':'Midwest','states':['17','18','26','39','55']},
 'West North Central':{'region':'Midwest','states':['19','20','27','29','31','38','46']},
 'South Atlantic':{'region':'South','states':['10','11','12','13','24','37','45','51','54']},
 'East South Central':{'region':'South','states':['01','21','28','47']},
 'West South Central':{'region':'South','states':['05','22','40','48']},
 'Mountain':{'region':'West','states':['04','08','16','30','32','35','49','56']},
 'Pacific':{'region':'West','states':['02','06','15','41','53']}}
lookup={fips:(division,d['region']) for division,d in divisions.items() for fips in d['states']}
feature_by_id={g['id']:g for g in doc['objects']['states']['geometries']}
used=[]
for div in divisions:
    used.extend(divisions[div]['states'])
features=[feature_by_id[x] for x in sorted(used) if x in feature_by_id]
coords=[p for f in features for ring in rings_for(f) for p in ring]
minx=min(x for x,y in coords); maxx=max(x for x,y in coords); miny=min(y for x,y in coords); maxy=max(y for x,y in coords)
width=960;height=590;pad=8;scale=min((width-2*pad)/(maxx-minx),(height-2*pad)/(maxy-miny))
def xy(p): return (pad+(p[0]-minx)*scale,height-pad-(p[1]-miny)*scale)
parts=[f'<svg viewBox="0 0 {width} {height}" role="group" aria-label="Map of the United States colored by Census division" xmlns="http://www.w3.org/2000/svg">']
for div,info in divisions.items():
    fid=[feature_by_id[x] for x in info['states'] if x in feature_by_id]
    state_names=', '.join(f['properties']['name'] for f in fid)
    title=f'Select {div}, Census division. This value represents the division, which includes: {state_names}.'
    parts.append(f'<g class="division-shape" data-division="{html.escape(div)}" data-region="{info["region"]}" role="button" tabindex="0" aria-label="{html.escape(title)}">')
    for f in fid:
        path=[]
        for ring in rings_for(f):
            pts=[xy(p) for p in ring]
            if not pts: continue
            path.append('M '+' L '.join(f'{x:.2f},{y:.2f}' for x,y in pts)+' Z')
        parts.append(f'<path class="state-shape" data-state="{html.escape(f["properties"]["name"])}" d="{" ".join(path)}" aria-hidden="true"/>')
    parts.append('</g>')
parts.append('</svg>')
Path('data/us-map.svg').write_text('\n'.join(parts)+'\n')
