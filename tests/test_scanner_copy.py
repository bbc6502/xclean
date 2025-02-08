import os

from tests.fixtures import Fixtures


class TestCase(Fixtures):

    def test_archive_duplicates_copy(
            self,
            scanner,
            master_dir_path, duplicate_dir_path, archive_dir_path,
            m_file1, d_file1
    ):
        scanner.scan(dir_path=master_dir_path)
        results = scanner.clean(
            dir_path=duplicate_dir_path,
            archive_to=archive_dir_path,
            copy=True,
        )
        assert results == {
            'duplicates': {
                'count': 1,
                'size': 1500,
            },
            'files': {
                'count': 1,
                'size': 1500,
            },
            'new': {
                'count': 0,
                'size': 0,
            },
            'abort': False,
        }
        assert len(os.listdir(master_dir_path)) == 1
        assert len(os.listdir(os.path.dirname(d_file1))) == 1
        assert len(os.listdir(archive_dir_path)) == 1
