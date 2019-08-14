from operations.repo import create_repo
import pytest

def test_creat_repos(env):
    result = create_repo(env.github,'yuyuyu')
    print(result.success)
    assert result.success == True, result.error
if __name__=="__main__":
    pytest.main()