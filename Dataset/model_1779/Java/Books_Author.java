





import java.util.List;
import java.util.ArrayList;

public class Books_Author  {

    private String name;





    private Books_Book books_book;




    private List<Books_Book> books_books;




    private Books_System books_system;


    public Books_Author(
        String name    ) {
        this.name = name;
        this.books_books = new ArrayList<>();
    }

    public Books_Author(
        String name        ArrayList<Books_Book> books_books    ) {
        this.name = name;
        this.books_books = books_books;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Books_Book getBooks_book() {
        return books_book;
    }

    public void setBooks_book(Books_Book books_book) {
        this.books_book = books_book;
    }
    public List<Books_Book> getBooks_books() {
        return books_books;
    }

    public void addBooks_book(Books_book books_book) {
        this.books_books.add(books_book);
    }
    public Books_System getBooks_system() {
        return books_system;
    }

    public void setBooks_system(Books_System books_system) {
        this.books_system = books_system;
    }

}