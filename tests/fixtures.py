import os

import pytest

from xclean.scanner import Scanner


class Fixtures:

    @pytest.fixture
    def scanner(self):
        scanner = Scanner(db_path=':memory:')
        return scanner

    @pytest.fixture
    def scanner_ignore_existing(self):
        scanner = Scanner(db_path=':memory:', ignore_existing=True)
        return scanner

    @pytest.fixture
    def scanner_with_copy(self):
        scanner = Scanner(db_path=':memory:', copy=True)
        return scanner

    @pytest.fixture
    def scanner_with_prompt(self):
        scanner = Scanner(db_path=':memory:', prompt=True)
        return scanner

    @pytest.fixture
    def file_name_1(self):
        return 'file1.jpg'

    @pytest.fixture
    def file_name_2(self):
        return 'file2.jpg'

    @pytest.fixture
    def file_name_3(self):
        return 'file3.png'

    @pytest.fixture
    def file_name_4(self):
        return 'file4.png'

    @pytest.fixture
    def file_name_5(self):
        return 'file5'

    @pytest.fixture(autouse=True)
    def clean_temporary_files(self, scanner, file_name_1, file_name_2):
        trash_dir_path = scanner.trash_directory()
        if trash_dir_path is not None:
            for file_name in (file_name_1, file_name_2):
                file_path = os.path.join(trash_dir_path, file_name)
                if os.path.exists(file_path):
                    os.remove(file_path)

    @pytest.fixture
    def master_dir_path(self, tmp_path):
        master_dir_path = os.path.join(tmp_path, 'master')
        if not os.path.exists(master_dir_path):
            os.mkdir(master_dir_path)
        return master_dir_path

    @pytest.fixture
    def duplicate_dir_path(self, tmp_path):
        duplicate_dir_path = os.path.join(tmp_path, 'duplicate')
        if not os.path.exists(duplicate_dir_path):
            os.mkdir(duplicate_dir_path)
        return duplicate_dir_path

    @pytest.fixture
    def duplicate_sub_dir_path(self, duplicate_dir_path):
        sub_dir_path = os.path.join(duplicate_dir_path, 'subdir')
        if not os.path.exists(sub_dir_path):
            os.mkdir(sub_dir_path)
        return sub_dir_path

    @pytest.fixture
    def archive_dir_path(self, tmp_path):
        archive_dir_path = os.path.join(tmp_path, 'archive')
        if not os.path.exists(archive_dir_path):
            os.mkdir(archive_dir_path)
        return archive_dir_path

    @pytest.fixture
    def archive_sub_dir_path(self, archive_dir_path):
        archive_dir_path = os.path.join(archive_dir_path, 'subdir')
        if not os.path.exists(archive_dir_path):
            os.mkdir(archive_dir_path)
        return archive_dir_path

    @pytest.fixture
    def newfiles_dir_path(self, tmp_path):
        archive_dir_path = os.path.join(tmp_path, 'newfiles')
        if not os.path.exists(archive_dir_path):
            os.mkdir(archive_dir_path)
        return archive_dir_path

    @pytest.fixture
    def newfiles_sub_dir_path(self, newfiles_dir_path):
        archive_dir_path = os.path.join(newfiles_dir_path, 'subdir')
        if not os.path.exists(archive_dir_path):
            os.mkdir(archive_dir_path)
        return archive_dir_path

    @pytest.fixture
    def db_file(self, tmp_path):
        db_file = os.path.join(tmp_path, 'db.sqlite3')
        return db_file

    @pytest.fixture
    def m_file1(self, master_dir_path, file_name_1):
        m_file1 = os.path.join(master_dir_path, file_name_1)
        with open(m_file1, 'w') as fp:
            fp.write('a'*1500)
        return m_file1

    @pytest.fixture
    def m_file1_xmp1(self, master_dir_path, file_name_1):
        m_file1 = os.path.join(master_dir_path, f'{file_name_1}.xmp')
        with open(m_file1, 'w') as fp:
            fp.write('a'*150)
        return m_file1

    @pytest.fixture
    def m_file1_xmp2(self, master_dir_path, file_name_1):
        m_file1 = os.path.join(master_dir_path, f'{file_name_1}.XMP')
        with open(m_file1, 'w') as fp:
            fp.write('a'*150)
        return m_file1

    @pytest.fixture
    def m_file1_xmp3(self, master_dir_path, file_name_1):
        prefix, extn = os.path.splitext(file_name_1)
        m_file1 = os.path.join(master_dir_path, f'{prefix}.xmp')
        with open(m_file1, 'w') as fp:
            fp.write('a'*150)
        return m_file1

    @pytest.fixture
    def m_file1_xmp4(self, master_dir_path, file_name_1):
        prefix, extn = os.path.splitext(file_name_1)
        m_file1 = os.path.join(master_dir_path, f'{prefix}.XMP')
        with open(m_file1, 'w') as fp:
            fp.write('a'*150)
        return m_file1

    @pytest.fixture
    def m_file1_link(self, master_dir_path, m_file1):
        m_file1_link = os.path.join(master_dir_path, 'file1.link.txt')
        os.symlink(m_file1, m_file1_link)
        return m_file1_link

    @pytest.fixture
    def m_file2(self, master_dir_path, file_name_2):
        m_file2 = os.path.join(master_dir_path, file_name_2)
        with open(m_file2, 'w') as fp:
            fp.write('b'*1600)
        return m_file2

    @pytest.fixture
    def m_file2_xmp1(self, master_dir_path, file_name_2):
        m_file1 = os.path.join(master_dir_path, f'{file_name_2}.xmp')
        with open(m_file1, 'w') as fp:
            fp.write('a'*160)
        return m_file1

    @pytest.fixture
    def m_file3(self, master_dir_path, file_name_3):
        m_file3 = os.path.join(master_dir_path, file_name_3)
        with open(m_file3, 'w') as fp:
            fp.write('a'*1700)
        return m_file3

    @pytest.fixture
    def m_file4(self, master_dir_path, file_name_4):
        m_file4 = os.path.join(master_dir_path, file_name_4)
        with open(m_file4, 'w') as fp:
            fp.write('b'*1800)
        return m_file4

    @pytest.fixture
    def m_file5(self, master_dir_path, file_name_5):
        m_file5 = os.path.join(master_dir_path, file_name_5)
        with open(m_file5, 'w') as fp:
            fp.write('c'*1900)
        return m_file5

    @pytest.fixture
    def d_file1(self, duplicate_sub_dir_path, file_name_1):
        d_file1 = os.path.join(duplicate_sub_dir_path, file_name_1)
        with open(d_file1, 'w') as fp:
            fp.write('a'*1500)
        return d_file1

    @pytest.fixture
    def a_file1(self, archive_sub_dir_path, file_name_1):
        d_file1 = os.path.join(archive_sub_dir_path, file_name_1)
        with open(d_file1, 'w') as fp:
            fp.write('a'*1500)
        return d_file1

    @pytest.fixture
    def d_file1_xmp1(self, duplicate_sub_dir_path, file_name_1):
        d_file1 = os.path.join(duplicate_sub_dir_path, f'{file_name_1}.xmp')
        with open(d_file1, 'w') as fp:
            fp.write('a'*150)
        return d_file1

    @pytest.fixture
    def d_file1_xmp2(self, duplicate_sub_dir_path, file_name_1):
        m_file1 = os.path.join(duplicate_sub_dir_path, f'{file_name_1}.XMP')
        with open(m_file1, 'w') as fp:
            fp.write('a'*150)
        return m_file1

    @pytest.fixture
    def d_file1_xmp3(self, duplicate_sub_dir_path, file_name_1):
        prefix, extn = os.path.splitext(file_name_1)
        m_file1 = os.path.join(duplicate_sub_dir_path, f'{prefix}.xmp')
        with open(m_file1, 'w') as fp:
            fp.write('a'*150)
        return m_file1

    @pytest.fixture
    def d_file1_xmp4(self, duplicate_sub_dir_path, file_name_1):
        prefix, extn = os.path.splitext(file_name_1)
        m_file1 = os.path.join(duplicate_sub_dir_path, f'{prefix}.XMP')
        with open(m_file1, 'w') as fp:
            fp.write('a'*150)
        return m_file1

    @pytest.fixture
    def d_file2(self, duplicate_sub_dir_path, file_name_2):
        d_file2 = os.path.join(duplicate_sub_dir_path, file_name_2)
        with open(d_file2, 'w') as fp:
            fp.write('b'*1600)
        return d_file2

    @pytest.fixture
    def d_file2_xmp1(self, duplicate_sub_dir_path, file_name_2):
        d_file1 = os.path.join(duplicate_sub_dir_path, f'{file_name_2}.xmp')
        with open(d_file1, 'w') as fp:
            fp.write('a'*160)
        return d_file1

    @pytest.fixture
    def d_file3(self, duplicate_sub_dir_path, file_name_3):
        d_file3 = os.path.join(duplicate_sub_dir_path, file_name_3)
        with open(d_file3, 'w') as fp:
            fp.write('a'*1700)
        return d_file3

    @pytest.fixture
    def d_file3_1(self, duplicate_sub_dir_path, file_name_3):
        d_file3 = os.path.join(duplicate_sub_dir_path, file_name_3)
        with open(d_file3, 'w') as fp:
            fp.write('a'*1500)
        return d_file3

    @pytest.fixture
    def d_file3_xmp1(self, duplicate_sub_dir_path, file_name_3):
        d_file1 = os.path.join(duplicate_sub_dir_path, f'{file_name_3}.xmp')
        with open(d_file1, 'w') as fp:
            fp.write('a'*170)
        return d_file1

    @pytest.fixture
    def d_file4(self, duplicate_sub_dir_path, file_name_4):
        d_file4 = os.path.join(duplicate_sub_dir_path, file_name_4)
        with open(d_file4, 'w') as fp:
            fp.write('b'*1800)
        return d_file4

    @pytest.fixture
    def d_file4_2(self, duplicate_sub_dir_path, file_name_4):
        d_file4 = os.path.join(duplicate_sub_dir_path, file_name_4)
        with open(d_file4, 'w') as fp:
            fp.write('b'*1600)
        return d_file4

    @pytest.fixture
    def d_file4_xmp1(self, duplicate_sub_dir_path, file_name_4):
        d_file1 = os.path.join(duplicate_sub_dir_path, f'{file_name_4}.xmp')
        with open(d_file1, 'w') as fp:
            fp.write('a'*180)
        return d_file1
