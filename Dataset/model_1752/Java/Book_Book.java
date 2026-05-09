





import java.util.List;
import java.util.ArrayList;

public class Book_Book  {

    private String title;





    private Book_Library book_library;


    public Book_Book(
        String title    ) {
        this.title = title;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Book_Library getBook_library() {
        return book_library;
    }

    public void setBook_library(Book_Library book_library) {
        this.book_library = book_library;
    }

}