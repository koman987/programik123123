class Node:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.elements = []

    def set(self, row, col, value):
        # Перевірка на вихід за межі матриці
        if row >= self.rows or col >= self.cols:
            raise IndexError("Index out of range")

        # Перевірка, чи елемент вже існує
        for node in self.elements:
            if node.row == row and node.col == col:
                node.value = value
                return

        # Якщо елемента немає, додаємо новий вузол
        self.elements.append(Node(row, col, value))

    def get(self, row, col):
        for node in self.elements:
            if node.row == row and node.col == col:
                return node.value
        return 0  # Якщо елемента немає, повертаємо 0

    def __str__(self):
        # Перевизначення методу __str__ для зручного виведення
        result = ""
        for i in range(self.rows):
            for j in range(self.cols):
                result += str(self.get(i, j)).ljust(4)
            result += "\n"
        return result
matrix = SparseMatrix(3, 4)
matrix.set(0, 1, 2)
matrix.set(1, 2, 5)
print(matrix)