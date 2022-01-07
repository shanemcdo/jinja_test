#!/usr/bin/env python3

import os
from glob import glob
from jinja2 import Environment, FileSystemLoader, select_autoescape

target_dir = 'bin'

if __name__ == '__main__':
    environment = Environment(
        loader = FileSystemLoader('./templates'),
        autoescape = select_autoescape(['html', 'xml'])
    )
    blacklist = ['base.html.jinja']
    template_names = [name.split(os.sep, 2)[-1] for name in glob('./templates/**')]
    for name in template_names:
        if name in blacklist:
            continue
        elif not os.path.exists(target_dir):
            os.mkdir(target_dir)
        template = environment.get_template(name)
        with open(os.path.join(target_dir, name.replace('.jinja', '')), 'w') as f:
            f.write(template.render())
