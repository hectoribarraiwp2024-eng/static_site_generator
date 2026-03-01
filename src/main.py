import os
import shutil
from markdown_to_htmlnode import markdown_to_html_node

def main():
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

    public_path = os.path.join(PROJECT_ROOT, "public")
    static_path = os.path.join(PROJECT_ROOT, "static")

    clear_directory(public_path)
    copy_directory(static_path , public_path)

    content_path = os.path.join(PROJECT_ROOT, "content/index.md")
    template_path = os.path.join(PROJECT_ROOT, "template.html")
    index_path = os.path.join(public_path, "index.html")

    html_content = gernerate_page(content_path, template_path, public_path)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    glorfindel_content_path = os.path.join(PROJECT_ROOT, "content/blog/glorfindel/index.md")
    tom_content_path = os.path.join(PROJECT_ROOT, "content/blog/tom/index.md")
    majesty_content_path = os.path.join(PROJECT_ROOT, "content/blog/majesty/index.md")
    contact_content_path = os.path.join(PROJECT_ROOT, "content/contact/index.md")


    glorfindel_index_path = os.path.join(public_path, "blog/glorfindel/index.html")
    os.makedirs(os.path.dirname(glorfindel_index_path), exist_ok=True)
    tom_index_path = os.path.join(public_path, "blog/tom/index.html")
    os.makedirs(os.path.dirname(tom_index_path), exist_ok=True)
    majesty_index_path = os.path.join(public_path, "blog/majesty/index.html")
    os.makedirs(os.path.dirname(majesty_index_path), exist_ok=True)
    contact_index_path = os.path.join(public_path, "contact/index.html")
    os.makedirs(os.path.dirname(contact_index_path), exist_ok=True)

    ghtml_content = gernerate_page(glorfindel_content_path, template_path, public_path)

    with open(glorfindel_index_path, "w", encoding="utf-8") as f:
        f.write(ghtml_content)

    thtml_content = gernerate_page(tom_content_path, template_path, public_path)

    with open(tom_index_path, "w", encoding="utf-8") as f:
        f.write(thtml_content)

    mhtml_content = gernerate_page(majesty_content_path, template_path, public_path)

    with open(majesty_index_path, "w", encoding="utf-8") as f:
        f.write(mhtml_content)

    chtml_content = gernerate_page(contact_content_path, template_path, public_path)

    with open(contact_index_path, "w", encoding="utf-8") as f:
        f.write(chtml_content)
    
def clear_directory(path):
    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if os.path.isfile(full_path):
            os.remove(full_path)
        elif os.path.isdir(full_path):
            clear_directory(full_path)
            os.rmdir(full_path)

def copy_directory(src, dest):
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        elif os.path.isdir(src_path):
            os.makedirs(dest_path, exist_ok=True)
            copy_directory(src_path, dest_path)

def gernerate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    
    with open(from_path, 'r') as text:
        markdown = text.read()

    with open(template_path, 'r') as text:
        template = text.read()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    new_template = template.replace('{{ Title }}', title)
    new_template = new_template.replace('{{ Content }}', html)

    return new_template


    

def extract_title(markdown):
    if markdown.startswith('#'):
        markdown_lines = markdown.split('\n')
        title = markdown_lines[0].lstrip('# ').strip()
        return title
    raise Exception("There is no title")

main()