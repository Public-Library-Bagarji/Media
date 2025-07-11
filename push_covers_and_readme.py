import os
import subprocess
import shutil

# CONFIGURATION
COVERS_DIR = 'book covers'
README_PATH = 'README.md'
GITHUB_RAW_PREFIX = 'https://raw.githubusercontent.com/Public-Library-Bagarji/Media/main/book_covers/'

# 1. Copy new images to book_covers directory (if needed, but here we assume images are already there)
# (If you want to copy from another folder, add logic here)

# 2. Generate README.md in the root directory
def generate_readme():
    image_files = [f for f in os.listdir(COVERS_DIR)
                   if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif'))]
    image_files.sort()
    lines = [
        '# Public Library Bagarji - Book Cover Images',
        '',
        'Below are the book cover images stored in this repository. You can use the **Raw** URL for each image as an external cover image link in the admin panel. The book name is inferred from the file name.',
        '',
        '| Book Name | Image | Raw URL |',
        '|-----------|-------|---------|'
    ]
    for fname in image_files:
        book_name = os.path.splitext(fname)[0]
        raw_url = GITHUB_RAW_PREFIX + fname
        lines.append(f'| {book_name} | ![{book_name}]({raw_url}) | {raw_url} |')
    lines.append('\n---\n')
    lines.append('**How to use:**')
    lines.append('- Copy the Raw URL for the image you want.')
    lines.append('- Paste it in the "External cover image link" field in the admin panel for the relevant book.')
    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'Updated README.md with {len(image_files)} images.')

# 3. Git add/commit/push
def git_push():
    cmds = [
        ['git', 'add', COVERS_DIR],
        ['git', 'add', README_PATH],
        ['git', 'commit', '-m', 'Auto: add new book covers and update README.md'],
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
