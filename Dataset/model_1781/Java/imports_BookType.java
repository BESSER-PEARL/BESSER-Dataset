





import java.util.List;
import java.util.ArrayList;

public class imports_BookType  {

    private String title;
    private String author;
    private String isbn;



    public imports_BookType(
        String title,        String author,        String isbn    ) {
        this.title = title;
        this.author = author;
        this.isbn = isbn;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }


}