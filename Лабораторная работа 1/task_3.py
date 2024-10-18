# TODO Найдите количество книг, которое можно разместить на дискете
# Данные
disk_capacity_mb = 1.44
pages_per_book = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

# Объем дискеты в байтах
disk_capacity_bytes = disk_capacity_mb * 1024 * 1024

# Общее количество символов в книге
total_chars_per_book = pages_per_book * lines_per_page * chars_per_line

# Объем одной книги в байтах
book_size_bytes = total_chars_per_book * bytes_per_char

# Количество книг, помещающихся на дискету
number_of_books = int(disk_capacity_bytes / book_size_bytes)

print("Количество книг, помещающихся на дискету:", number_of_books)
