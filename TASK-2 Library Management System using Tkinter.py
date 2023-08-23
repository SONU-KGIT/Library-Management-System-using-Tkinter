import tkinter as tk
from tkinter import messagebox, ttk


class Book:
    def __init__(self, book_id, title, author, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                break

    def search_book(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        return found_books

    def display_books(self):
        return self.books


class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        

        self.library = Library()

        self.menu_label = tk.Label(root, text="Library Management System", font=("Helvetica", 18, "bold"), fg="blue")
        self.menu_label.pack(pady=10)

        self.add_frame = tk.Frame(root)
        self.add_frame.pack()

        self.add_label = tk.Label(self.add_frame, text="Add Book", font=("Helvetica", 14, "bold"))
        self.add_label.grid(row=0, columnspan=2, pady=5)

        self.id_label = tk.Label(self.add_frame, text="Book ID:")
        self.id_label.grid(row=1, column=0, sticky="e", padx=5)
        self.id_entry = tk.Entry(self.add_frame, width=20, font=("Arial", 12))
        self.id_entry.grid(row=1, column=1, padx=5)

        self.title_label = tk.Label(self.add_frame, text="Title:")
        self.title_label.grid(row=2, column=0, sticky="e", padx=5)
        self.title_entry = tk.Entry(self.add_frame,  width=20, font=("Arial", 12))
        self.title_entry.grid(row=2, column=1, padx=5)

        self.author_label = tk.Label(self.add_frame, text="Author:")
        self.author_label.grid(row=3, column=0, sticky="e", padx=5)
        self.author_entry = tk.Entry(self.add_frame)
        self.author_entry.grid(row=3, column=1, padx=5)

        self.genre_label = tk.Label(self.add_frame, text="Genre:")
        self.genre_label.grid(row=4, column=0, sticky="e", padx=5)
        self.genre_entry = tk.Entry(self.add_frame)
        self.genre_entry.grid(row=4, column=1, padx=5)

        self.add_button = tk.Button(self.add_frame, text="Add", command=self.add_book, bg="green", fg="white")
        self.add_button.grid(row=5, columnspan=2, pady=10)

        self.remove_frame = tk.Frame(root)
        self.remove_frame.pack()

        self.remove_label = tk.Label(self.remove_frame, text="Remove Book", font=("Helvetica", 14, "bold"))
        self.remove_label.grid(row=0, columnspan=2, pady=5)

        self.remove_id_label = tk.Label(self.remove_frame, text="Book ID:")
        self.remove_id_label.grid(row=1, column=0, sticky="e", padx=5)
        self.remove_id_entry = tk.Entry(self.remove_frame)
        self.remove_id_entry.grid(row=1, column=1, padx=5)

        self.remove_button = tk.Button(self.remove_frame, text="Remove", command=self.remove_book, bg="red", fg="white")
        self.remove_button.grid(row=2, columnspan=2, pady=10)

        self.search_frame = tk.Frame(root)
        self.search_frame.pack()

        self.search_label = tk.Label(self.search_frame, text="Search Book", font=("Helvetica", 14, "bold"))
        self.search_label.grid(row=0, columnspan=2, pady=5)

        self.search_title_label = tk.Label(self.search_frame, text="Title:")
        self.search_title_label.grid(row=1, column=0, sticky="e", padx=5)
        self.search_title_entry = tk.Entry(self.search_frame)
        self.search_title_entry.grid(row=1, column=1, padx=5)

        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_books)
        self.search_button.grid(row=2, columnspan=2, pady=10)

        self.display_frame = tk.Frame(root)
        self.display_frame.pack()

        self.display_label = tk.Label(self.display_frame, text="Display Books", font=("Helvetica", 14, "bold"))
        self.display_label.grid(row=0, columnspan=2, pady=5)
        self.display_listbox = tk.Listbox(self.display_frame, font=("Courier New", 12), bg="lightyellow",height=10,width=60)
        self.menu_label.pack(pady=15)
        self.add_frame.pack(padx=20, pady=10)
        self.display_listbox.grid(row=1, column=0, columnspan=2, pady=10)

        self.refresh_button = tk.Button(self.display_frame, text="Refresh", command=self.display_books)
        self.refresh_button.grid(row=2, columnspan=2, pady=5)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack(pady=10)

    def add_book(self):
        book_id = int(self.id_entry.get())
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()

        new_book = Book(book_id, title, author, genre)
        self.library.add_book(new_book)
        messagebox.showinfo("Success", "Book added successfully!")

        self.clear_add_fields()

    def remove_book(self):
        book_id = int(self.remove_id_entry.get())
        self.library.remove_book(book_id)
        messagebox.showinfo("Success", "Book removed successfully!")

        self.clear_remove_fields()

    def search_books(self):
        title = self.search_title_entry.get()
        found_books = self.library.search_book(title)
        if found_books:
            result = "Found Books:\n" + "\n".join([f"{book.title} by {book.author}" for book in found_books])
            messagebox.showinfo("Search Results", result)
        else:
            messagebox.showinfo("Search Results", "No books found with the given title.")

        self.clear_search_fields()

    def display_books(self):
        self.display_listbox.delete(0, tk.END)
        for book in self.library.display_books():
            availability = "Available" if book.available else "Not Available"
            book_info = f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Status: {availability}"
            self.display_listbox.insert(tk.END, book_info)

    def clear_add_fields(self):
        self.id_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)

    def clear_remove_fields(self):
        self.remove_id_entry.delete(0, tk.END)

    def clear_search_fields(self):
        self.search_title_entry.delete(0, tk.END)


def main():
    root = tk.Tk()
    app = LibraryApp
    app = LibraryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
