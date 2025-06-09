# tests/test_all.py

import unittest
import os
import shutil
from git_core.repo import init_repo
from git_core.index import add_files, read_index
from git_core.objects import hash_object
from git_core.commit import create_commit
from config.config import set_remote, get_remote_url

TEST_REPO = "test_repo"

class TestGitClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if os.path.exists(TEST_REPO):
            shutil.rmtree(TEST_REPO)
        os.makedirs(TEST_REPO)
        os.chdir(TEST_REPO)
        init_repo()

    def test_01_init_repo(self):
        self.assertTrue(os.path.exists(".git"))
        self.assertTrue(os.path.exists(os.path.join(".git", "objects")))
        self.assertTrue(os.path.exists(os.path.join(".git", "refs", "heads")))

    def test_02_add_file_to_index(self):
        with open("test.txt", "w") as f:
            f.write("Hello Git")
        add_files(["test.txt"])
        index = read_index()
        self.assertIn("test.txt", index)
        self.assertIn("oid", index["test.txt"])

    def test_03_hash_object(self):
        content = b"Sample content"
        oid = hash_object(content, "blob")
        self.assertEqual(len(oid), 40)
        from git_core.utils import resolve_object_path
        path = resolve_object_path(oid)
        self.assertTrue(os.path.exists(path))

    def test_04_create_commit(self):
        sha = create_commit("Initial commit")
        self.assertEqual(len(sha), 40)
        head_path = ".git/HEAD"
        with open(head_path) as f:
            ref_line = f.read().strip()
        self.assertTrue(ref_line.startswith("ref: "))
        commit_path = os.path.join(".git", ref_line[5:])
        with open(commit_path) as f:
            commit_sha = f.read().strip()
        self.assertEqual(sha, commit_sha)

    def test_05_config_set_and_get_remote(self):
        set_remote("origin", "https://github.com/example/repo.git") 
        url = get_remote_url("origin")
        self.assertEqual(url, "https://github.com/example/repo.git") 

    @classmethod
    def tearDownClass(cls):
        os.chdir("..")
        shutil.rmtree(TEST_REPO)

if __name__ == "__main__":
    unittest.main()