import os
import shutil
import subprocess

# 路径设定
UPLOAD_FOLDER = os.path.expanduser('~/Desktop/UploaderBox')
ARCHIVE_FOLDER = os.path.join(UPLOAD_FOLDER, 'uploaded_done')
GIT_REPO_PATH = os.path.expanduser('~/Desktop/YourGitRepo')  # ⛳ 请稍后改成你的 Git 仓库路径

# 创建归档文件夹
os.makedirs(ARCHIVE_FOLDER, exist_ok=True)

# 只上传 .pdf 文件
files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.pdf')]

for filename in files:
    src_path = os.path.join(UPLOAD_FOLDER, filename)
    dst_path = os.path.join(ARCHIVE_FOLDER, filename)
    repo_file_path = os.path.join(GIT_REPO_PATH, filename)

    # 拷贝文件进 GitHub 仓库文件夹
    shutil.copy2(src_path, repo_file_path)

    # Git 添加、提交、推送
    subprocess.run(['git', '-C', GIT_REPO_PATH, 'add', filename])
    subprocess.run(['git', '-C', GIT_REPO_PATH, 'commit', '-m', f'Auto upload {filename}'])
    subprocess.run(['git', '-C', GIT_REPO_PATH, 'push'])

    # 原文件移入归档区，避免重复上传
    shutil.move(src_path, dst_path)

print("✅ 全部上传成功并归档完毕。")
