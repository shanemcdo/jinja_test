from glob import glob
from jinja2 import Environment, FileSystemLoader, select_autoescape

if __name__ == '__main__':
    environment = Environment(
            loader = FileSystemLoader('.\\templates'),
            autoescape = select_autoescape(['html', 'xml'])
            )
    blacklist = ['base.html.jinja']
    template_names = [name.split('\\', 2)[-1] for name in glob('.\\templates/**')]
    for name in template_names:
        if name in blacklist:
            continue
        template = environment.get_template(name)
        with open('.\\bin\\' + name.replace('.jinja', ''), 'w') as f:
            f.write(template.render())
