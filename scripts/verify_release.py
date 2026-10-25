"""Validate manifest + Skill layout using only Python's stdlib."""
import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'RELEASE_MANIFEST.json').read_text(encoding='utf-8'))
assert manifest['history_inherited'] is False
registered={x['path'] for x in manifest['files']}
assert not any(
    any(part in ('__pycache__','.pytest_cache','.git','.venv') for part in Path(path).parts)
    or path.endswith(('.pyc','.pyo','.DS_Store'))
    for path in registered
), 'Runtime caches must never enter a release manifest'

for m in manifest['files']:
    p=root/m['path']
    assert p.is_file() and p.stat().st_size==m['bytes'],m['path']
    assert hashlib.sha256(p.read_bytes()).hexdigest()==m['sha256'],m['path']
assert len(registered)==len(manifest['files'])
for area in ('01-Information-Acquisition','02-Research','03-Development','04-Media',
             '05-Career','06-Documents','07-Knowledge-Management','08-Special'):
    children={p.name for p in (root/area).iterdir() if p.is_dir()}
    assert children=={'Skills','Plugins','MCPs'},(area,children)
catalog=json.loads((root/'catalog.json').read_text(encoding='utf-8'))
assert catalog['skill_count']==len(catalog['included'])==11
for item in catalog['included']:
    skill=root/item['skill']/'SKILL.md'
    assert skill.is_file()
    content=skill.read_text(encoding='utf-8')
    assert content.startswith('---\n') and '\nname:' in content[:250],skill
    assert all((root/f).is_file() for f in item['files'])
for path in root.rglob('*'):
    if path.is_file() and '.git' not in path.parts and path.name!='RELEASE_MANIFEST.json':
        assert str(path.relative_to(root)) in registered,path
print('PASS: 8x3 taxonomy; 11 Skills; offline integrity; no unlisted files')
