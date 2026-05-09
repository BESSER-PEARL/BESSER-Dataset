





import java.util.List;
import java.util.ArrayList;

public class Book_Chapter  {

    private String title;





    private Book_Book book_book;


    public Book_Chapter(
        String title    ) {
        this.title = title;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Book_Book getBook_book() {
        return book_book;
    }

    public void setBook_book(Book_Book book_book) {
        this.book_book = book_book;
    }

}