from src import run
from src.errors import ExpectedError

if __name__ == '__main__':
    try:
        run.main()
    except ExpectedError as e:
        print(e)
    except Exception as e:
        print(f"Unexpected error: {e}")