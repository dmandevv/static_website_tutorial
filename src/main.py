from textnode import * 
from htmlnode import *
from functions import *
from pathlib import Path

import os
import shutil
import sys

dir_static_path = "./static"
dir_public_path = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    basepath = sys.argv[0] if len(sys.argv) > 0 else "/"

    if os.path.exists(dir_public_path):
        print("Deleting public directory...")
        shutil.rmtree(dir_public_path)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_static_path, dir_public_path)
    
    print("Generating page...")
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_public_path,
        basepath
    )

    


def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if "<h1>" in line:
            return line.lstrip("<h1>").rstrip("</h1>").strip(" ")
    raise Exception(f"No 'h1' header found in: {markdown}")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    
    markdown_file = open(from_path, "r")
    markdown_content = markdown_file.read()
    markdown_file.close()

    template_file = open(template_path, "r")
    template_content = template_file.read()
    template_file.close()


    html = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(html)

    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html)
    template_content = template_content.replace('href="/', 'href="' + basepath)
    template_content = template_content.replace('src="/', 'src="' + basepath)

    dest_dir_path = os.path.dirname(dest_path)

    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)

if __name__ == '__main__':
    main()