from admin import Admin
from operations_manager import OperationsManager


def main():
    admin = Admin()
    manager = OperationsManager(admin)
    manager.menu()


if __name__ == "__main__":
    main()