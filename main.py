import matplotlib.pyplot as plt
import numpy as np

laptops_by_char = {
    "Процессор (ГГц)": {"ASUS ROG Strix": 2.6, "Lenovo Legion 5": 3.0, "HP Omen 15": 2.8, "MSI GF65": 2.5},
    "ОЗУ (ГБ)": {"ASUS ROG Strix": 16, "Lenovo Legion 5": 32, "HP Omen 15": 16, "MSI GF65": 16},
    "SSD (ГБ)": {"ASUS ROG Strix": 512, "Lenovo Legion 5": 1000, "HP Omen 15": 512, "MSI GF65": 256},
    "Видеокарта (ГБ)": {"ASUS ROG Strix": 8, "Lenovo Legion 5": 6, "HP Omen 15": 4, "MSI GF65": 6},
    "Экран (дюймы)": {"ASUS ROG Strix": 15.6, "Lenovo Legion 5": 15.6, "HP Omen 15": 15.6, "MSI GF65": 15.6},
    "Вес (кг)": {"ASUS ROG Strix": 2.4, "Lenovo Legion 5": 2.7, "HP Omen 15": 2.3, "MSI GF65": 2.1}
}

models = list(next(iter(laptops_by_char.values())).keys())
char_names = list(laptops_by_char.keys())
data_matrix = [[laptops_by_char[char][model] for char in char_names] for model in models]

def get_normal(matrix):
    base_row = matrix[0]
    return [[v / b for v, b in zip(row, base_row)] for row in matrix]

def get_quality(normalized_matrix):
    return [round(sum(row) / len(row), 2) for row in normalized_matrix]

def create_bar(names, values):
    plt.figure(figsize=(10, 6))
    plt.bar(names, values, color='skyblue', edgecolor='black')
    plt.xlabel("Модель")
    plt.ylabel("Kту (коэффициент качества)")
    plt.title("Сравнение моделей по качеству", pad=15)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def create_radial(models_list, labels, normalized_matrix):
    closed_data = [row + row[:1] for row in normalized_matrix]
    count = len(labels)
    angles = np.linspace(0, 2 * np.pi, count, endpoint=False).tolist()
    angles += angles[:1]
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection="polar"))
    for i, data_row in enumerate(closed_data):
        ax.plot(angles, data_row, "o-", linewidth=2, label=models_list[i])
        ax.fill(angles, data_row, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=10)
    ax.set_ylim(0, 2)
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.0))
    plt.title("Сравнение относительных характеристик", pad=20)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    normalized_data = get_normal(data_matrix)
    quality_scores = get_quality(normalized_data)
    create_bar(models, quality_scores)
    create_radial(models, char_names, normalized_data)