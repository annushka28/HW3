import csv
import random
import os
import sys

NUM_ROWS = 50


COLUMNS = ["Бравлер", "Редкость", "Кубки", "Здоровье"]

def generate_row():

    return {
        "Бравлер": random.choice(["Поко", "Эль Примо", "Биби", "Дэррил", "Пэм", "Фрэнк", "Гэйл", "Макс", "Мистер П", "Тара", "Спайк", "Колетт", "Рико", "Динамайк", "Мортис"]),
        "Редкость": random.choice(["Обычный", "Редкий", "Эпический", "Легендарный"]),
        "Кубки": random.randint(0, 100000),
        "Здоровье": random.randint(1000, 10000)
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)

