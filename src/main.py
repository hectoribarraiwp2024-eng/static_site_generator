import os
import shutil
from markdown_to_htmlnode import markdown_to_html_node
from pathlib import Path
import sys


dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
if sys.argv[1] == None:
    base_path = '/'
else:
    base_path = sys.argv[1]

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to public directory...")
    copy_directory(dir_path_static, dir_path_docs)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs)

    
def clear_directory(path):
    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if os.path.isfile(full_path):
            os.remove(full_path)
        elif os.path.isdir(full_path):
            clear_directory(full_path)
            os.rmdir(full_path)

def copy_directory(src, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)

    for filename in os.listdir(src):
        from_path = os.path.join(src, filename)
        dest_path = os.path.join(dest, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_directory(from_path, dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    
    with open(from_path, 'r') as text:
        markdown = text.read()

    with open(template_path, 'r') as text:
        template = text.read()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace('{{ Title }}', title)
    template = template.replace('{{ Content }}', html)
    template = template.replace('href="/', f'href="{base_path}')
    template = template.replace('src="/', f'src="{base_path}')
    print(base_path)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)



    

def extract_title(markdown):
    if markdown.startswith('#'):
        markdown_lines = markdown.split('\n')
        title = markdown_lines[0].lstrip('# ').strip()
        return title
    raise Exception("There is no title")

main()