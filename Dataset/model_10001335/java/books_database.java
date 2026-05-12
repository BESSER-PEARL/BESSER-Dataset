





import java.util.List;
import java.util.ArrayList;

public class books_database  {

    private String author;
    private String book_id;
    private String book_title;





    private library library;


    public books_database(
        String author,        String book_id,        String book_title    ) {
        this.author = author;
        this.book_id = book_id;
        this.book_title = book_title;
    }


    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getBook_id() {
        return book_id;
    }

    public void setBook_id(String book_id) {
        this.book_id = book_id;
    }
    public String getBook_title() {
        return book_title;
    }

    public void setBook_title(String book_title) {
        this.book_title = book_title;
    }

    public library getLibrary() {
        return library;
    }

    public void setLibrary(library library) {
        this.library = library;
    }

}