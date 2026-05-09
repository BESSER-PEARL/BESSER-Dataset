





import java.util.List;
import java.util.ArrayList;

public class book_Book  {

    private String bookId;
    private String author;
    private String title;
    private String resolution;
    private String version;
    private String description;



    public book_Book(
        String bookId,        String author,        String title,        String resolution,        String version,        String description    ) {
        this.bookId = bookId;
        this.author = author;
        this.title = title;
        this.resolution = resolution;
        this.version = version;
        this.description = description;
    }


    public String getBookid() {
        return bookId;
    }

    public void setBookid(String bookId) {
        this.bookId = bookId;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getResolution() {
        return resolution;
    }

    public void setResolution(String resolution) {
        this.resolution = resolution;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}