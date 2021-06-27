from jinja2 import Environment
from jinja2.loaders import FileSystemLoader
import os, os.path,errno, shutil

#################### CONSTANTS ####################
TEMPLATE_FOLDER = "templates"
GENERATE_TO_FOLDER = "."
SRC_PATH = "templates/src"
###################################################

#################### UTILITY FUNCTIONS ####################
def mkdir_p(path):
    '''attempts to make the folder if it doesnt exist
    '''
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def safe_open_w(path):
    '''Opens [path] for writing, creating any parent directories as needed
    '''
    mkdir_p(os.path.dirname(path))
    return open(path, 'w', encoding="utf8")

def WriteTo(file: str, data: str):
    '''Writes [data] to [file], while creating the parent directories and file if they do not exist
    '''
    path = f"{GENERATE_TO_FOLDER}/{file}"
    opened_file = safe_open_w(path=path)
    opened_file.write(data)
    opened_file.close()
###########################################################

environment = Environment(loader=FileSystemLoader(TEMPLATE_FOLDER))
'''[environment] is used by the jinja to know where the templates are when inheriting'''

templates: list[str] = []
'''will hold the path to all files that will be found in [TEMPLATE_FOLDER] folder'''

for root, dirs, files in os.walk(TEMPLATE_FOLDER):
    for f in files:
        path_to_file = os.path.relpath(os.path.join(root, f), ".")
        templates.append(path_to_file)

if not os.path.isdir(GENERATE_TO_FOLDER): os.mkdir(GENERATE_TO_FOLDER)
'''Creates the [GENERATE_TO_FOLDER] folder if it does not exist'''



for template in templates:
    '''this for loop will go through each file and attempt to render it if it is an html file and is not base.html'''

    if "base.html" in template.lower(): continue

    
    save_to = template.removeprefix(TEMPLATE_FOLDER + "\\") #this is where the file will be saved, (keeping structure of the original [TEMPLATE_FOLDER] folder)

    if not template.lower().endswith(".html"):
        '''if the file is not an html file, do not attempt to render
        simply save it while keeping its relative position to [TEMPLATE_FOLDER]
        '''
        mkdir_p(os.path.dirname(save_to))
        shutil.copyfile(template, save_to)

        continue

    #path_to_src = os.path.relpath(SRC_PATH, os.path.dirname(template)) \
    #                .replace(TEMPLATE_FOLDER + "\\", "")               \
    #                .replace("\\","/")
    #'''[path_to_src] is the relative path to src in the structure, this is used to correctly reference the src file no matter where a template is'''
    data = "".join(open(template, encoding="utf8").readlines()) #Gets the text content from the [template] file
    rendered = environment.from_string(data).render(path_to_src="src")
    WriteTo(file=save_to, data=rendered)
