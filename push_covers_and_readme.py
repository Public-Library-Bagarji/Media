import os
import subprocess
import shutil

# CONFIGURATION
IMAGE_DIRS = [
    ('book_covers', 'Book Covers'),
    ('Blog_Images', 'Blog Images'),
    ('Book_Review_Img', 'Book Review Images'),
    ('News_img', 'News Images'),
]
README_PATH = 'README.md'
GITHUB_RAW_BASE = 'https://raw.githubusercontent.com/Public-Library-Bagarji/Media/main/'

# 2. Generate README.md in the root directory

def generate_readme():
    lines = [
        '# Public Library Bagarji - Media Images',
        '',
        'Below are the images stored in this repository. Each section is for a different type of image. You can use the **Raw** URL for each image as an external link in the admin panel. The list is sorted alphabetically (A-Z) by image name.',
        ''
    ]
    for dir_name, section_title in IMAGE_DIRS:
        if not os.path.exists(dir_name):
            continue
        image_files = [f for f in os.listdir(dir_name)
                       if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif'))]
        image_files.sort(key=lambda x: os.path.splitext(x)[0].lower())
        lines.append(f'## {section_title}\n')
        if image_files:
            lines.append('| Name | Image | Raw URL |')
            lines.append('|------|-------|---------|')
    for fname in image_files:
                img_name = os.path.splitext(fname)[0]
                raw_url = f'{GITHUB_RAW_BASE}{dir_name}/{fname}'
                lines.append(f'| {img_name} | ![{img_name}]({raw_url}) | {raw_url} |')
    else:
            lines.append('_No images yet in this section._')
            lines.append('')
    lines.append('---')
    lines.append('**How to use:**')
    lines.append('- Copy the Raw URL for the image you want.')
    lines.append('- Paste it in the relevant field in the admin panel.')
    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'Updated README.md for all image directories.')

# 3. Git add/commit/push

def git_push():
    cmds = [
        ['git', 'add', README_PATH],
    ]
    for dir_name, _ in IMAGE_DIRS:
        cmds.append(['git', 'add', dir_name])
    cmds += [
        ['git', 'commit', '-m', 'Auto: add new images and update README.md for all directories'],
        ['git', 'push']
    ]
    for cmd in cmds:
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f'Git command failed: {e}')

if __name__ == '__main__':
    generate_readme()
    git_push()
    print('All done!') 
