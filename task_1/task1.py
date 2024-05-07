from pathlib import Path
import shutil
import os


def check_folder(path, destination_dir):
    try:
        if path.is_dir():
            for child in path.iterdir():
                check_folder(child, destination_dir)
        else:
            # Отримання формату файлу
            file_format = path.suffix.lower()

            # Шлях до папки з назвою формату
            format_dir = Path(destination_dir) / file_format[1:]

            # Створення папки з назвою формату, якщо вона ще не існує
            os.makedirs(format_dir, exist_ok=True)

            # Шлях до копійованого файлу
            destination_file = format_dir / path.name

            # Копіювання файлу у відповідну папку з назвою формату
            shutil.copy(path, destination_file)

    except Exception as e:
        print(f"Помилка обробки файлу {path}: {e}")


def recursive_walk(source_path, destination_path=None):
    try:
        if destination_path is None:
            # Ім'я нової папки
            new_folder_name = "dist"

            # Побудова шляху до нової папки поруч з заданою
            new_folder_path = os.path.join(
                os.path.dirname(source_path), new_folder_name
            )

            # Створення нової папки
            os.mkdir(new_folder_path)
            destination_path = new_folder_path

        check_folder(source_path, destination_path)

    except Exception as e:
        print(f"Помилка обробки папки {source_path}: {e}")


if __name__ == "__main__":
    root = Path(
        "/Users/avlady/Desktop/GOIT/Algorithms/goit-algo-hw-03/goit-algo-hw-03/task_1"
    )
    destin = Path(
        "/Users/avlady/Desktop/GOIT/Algorithms/goit-algo-hw-03/goit-algo-hw-03/Destination"
    )

    recursive_walk(root, destin)
