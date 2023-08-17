import sys

def generate_histogram(data, num_classes=10, class_width=50):
    histogram = [0] * num_classes
    for qtd, _ in data:
        class_index = min(qtd // class_width, num_classes - 1)
        histogram[class_index] += 1

    return histogram

def print_histogram(histogram, num_classes=10, class_width=50):
    for i in range(num_classes):
        lower_bound = i * class_width
        upper_bound = (i + 1) * class_width - 1 if i < num_classes - 1 else "+"
        print(f"{lower_bound}-{upper_bound}: {histogram[i]}")

def main():
    # abrir o arquivo
    file_name = sys.argv[1]
    with open(file_name, "r") as file:
        lines = file.readlines()

    # transformar as linhas do arquivo em um objeto iterável
    data = [(int(qtd), palavra.strip()) for qtd, palavra in (line.split() for line in lines)]

    histogram = generate_histogram(data)
    print_histogram(histogram)

if __name__ == "__main__":
    main()