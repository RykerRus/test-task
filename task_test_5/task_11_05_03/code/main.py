import sys
from backup_manager import BackupManager

if __name__ == "__main__":
    try:
        if (len(sys.argv) == 2):
            project_name = sys.argv[1]

            backup_manager = BackupManager()
            backup_manager.copy(project_name)
        else:
            project_name = input("Введите название проекта: ")

            backup_manager = BackupManager()
            backup_manager.copy(project_name)
    except Exception as err:
        print("Во время работы программы произошла ошибка! - {}"
              .format(err))
