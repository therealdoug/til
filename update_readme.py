import pathlib
import string
import json
from pprint import pprint
from jinja2 import Template

root = pathlib.Path(__file__).parent.resolve()

# This will be our document list as JSON object.  We'll use JINJA2 to turn it into 
# a markdown formatted README file.
readme_list = {}

def build_database(repo_path):
    for filepath in sorted(root.glob("*/*.md")):
        fp = filepath.open()
        title = str(fp.readline().lstrip("#").strip())
        path = str(filepath.relative_to(root))
        topic = str(path.split("/")[0])
        # readme_list[topic] = { title : path }
        if topic not in readme_list:
            readme_list[topic] = [{"title" : title, "path": path}]
        else:
            readme_list[topic].append({"title" : title, "path": path})


tm = Template(
("""
{%- for topic in readme_list %}
# {{ topic }}
{% for entry in readme_list[topic] %}
- [{{ entry.title }}]({{ entry.path }})
{%- endfor %}
{% endfor %}
""")
)


if __name__ == "__main__":
    build_database(root)

# Send to JINJA2 templating engine and return
msg = tm.render(readme_list=readme_list)

# Write it to file
with open('README.md', 'w') as f:
    f.write(msg)