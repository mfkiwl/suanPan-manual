import os
import platform
import re
import urllib.request
import shutil
import zipfile

from setuptools import setup


def remove(path: str):
    if os.path.exists(path):
        shutil.rmtree(path)


def install():
    # root directory
    remove('docs/Doxygen')

    doxygen_bin = 'doxygen'

    # if platform.system() == 'Linux':
    #     doxygen_tar = 'doxygen-1.9.4.linux.bin.tar.gz'
    #     url = f'https://www.doxygen.nl/files/{doxygen_tar}'
    #     with urllib.request.urlopen(url) as response, open(doxygen_tar, 'wb') as archive:
    #         shutil.copyfileobj(response, archive)
    #     shutil.unpack_archive(doxygen_tar, 'doxygen')
    #     os.remove(doxygen_tar)
    #     doxygen_bin = '../doxygen/doxygen-1.9.4/bin/doxygen'

    archive_name = 'suanPan-dev'

    url = 'https://github.com/TLCFEM/suanPan/archive/refs/heads/dev.zip'
    with urllib.request.urlopen(url) as response, open(f'{archive_name}.zip', 'wb') as archive:
        shutil.copyfileobj(response, archive)
    with zipfile.ZipFile(f'{archive_name}.zip', 'r') as archive:
        archive.extractall('.')
    os.remove(f'{archive_name}.zip')

    os.chdir(archive_name)

    os.system(doxygen_bin)

    target_path = '../docs/Doxygen'
    shutil.copytree('Document/html', target_path)
    shutil.copytree('Resource', f'{target_path}/Resource/')
    shutil.copy('../docs/favicon.ico', f'{target_path}/favicon.ico')

    with open('Toolbox/argumentParser.cpp') as f:
        version_file = f.read()

    major = re.search(r'constexpr auto SUANPAN_MAJOR = (\d);', version_file).group(1)
    minor = re.search(r'constexpr auto SUANPAN_MINOR = (\d);', version_file).group(1)
    patch = re.search(r'constexpr auto SUANPAN_PATCH = (\d);', version_file).group(1)

    os.chdir('..')

    remove(archive_name)
    remove('doxygen')

    with open('requirements.txt') as f:
        required = f.read().splitlines()

    setup(
        name='suanPan-manual',
        version=f'{major}.{minor}.{patch}',
        description='suanPan-manual',
        author='Theodore Chang',
        author_email='tlcfem@gmail.com',
        install_requires=required)


if __name__ == '__main__':
    install()
