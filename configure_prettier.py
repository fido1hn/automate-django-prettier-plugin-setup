"""
This module is designed to automate the extra steps needed to 
setup and use the awesome 'prettier-plugin-django-alpine' plugin 
for the prettier formatter in VSCode for your Django templates.

Requirements:
    - VSCode
    - VSCode Prettier extension(must be installed via extensions tab in VSCode)

    
Automated Steps:
    - prettier(local installation from npm)
        - npm install --save-dev --save-exact prettier
    - prettier-plugin-django-alpine
        - npm install --save-dev prettier-plugin-django-alpine
    - add .prettierrc file to the project root
        - {
            "plugins": ["prettier-plugin-django-alpine"]
        }
"""

import os


prettier_plugin = "prettier-plugin-django-alpine"
os.system("npm install --save-dev --save-exact prettier")
os.system(f"npm install --save-dev {prettier_plugin}")
with open(".prettierrc", "w") as f:
    f.write("{\n")
    f.write('    "plugins": ["prettier-plugin-django-alpine"]\n')
    f.write("}\n")
