from pathlib import Path
import pytest


def main():
    tests_path = Path(__file__).parent/"tests"
    pytest.main(["-v", str(tests_path)])


if __name__ == "__main__":
    main()
