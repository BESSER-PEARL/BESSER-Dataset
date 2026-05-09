





import java.util.List;
import java.util.ArrayList;

public class Book_Author  {

    private String name;





    private Book_Library book_library;




    private Book_Book book_book;


    public Book_Author(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Book_Library getBook_library() {
        return book_library;
    }

    public void setBook_library(Book_Library book_library) {
        this.book_library = book_library;
    }
    public Book_Book getBook_book() {
        return book_book;
    }

    public void setBook_book(Book_Book book_book) {
        this.book_book = book_book;
    }

}