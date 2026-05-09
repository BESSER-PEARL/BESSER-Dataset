





import java.util.List;
import java.util.ArrayList;

public class book_Book  {

    private String version;
    private String description;
    private String resolution;
    private String title;
    private String author;
    private String bookId;





    private book_Splash book_splash;




    private book_Page book_page;




    private List<book_Page> book_pages;


    public book_Book(
        String version,        String description,        String resolution,        String title,        String author,        String bookId    ) {
        this.version = version;
        this.description = description;
        this.resolution = resolution;
        this.title = title;
        this.author = author;
        this.bookId = bookId;
        this.book_pages = new ArrayList<>();
    }

    public book_Book(
        String version,        String description,        String resolution,        String title,        String author,        String bookId        ArrayList<book_Page> book_pages    ) {
        this.version = version;
        this.description = description;
        this.resolution = resolution;
        this.title = title;
        this.author = author;
        this.bookId = bookId;
        this.book_pages = book_pages;
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
    public String getResolution() {
        return resolution;
    }

    public void setResolution(String resolution) {
        this.resolution = resolution;
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
    public String getBookid() {
        return bookId;
    }

    public void setBookid(String bookId) {
        this.bookId = bookId;
    }

    public book_Splash getBook_splash() {
        return book_splash;
    }

    public void setBook_splash(book_Splash book_splash) {
        this.book_splash = book_splash;
    }
    public book_Page getBook_page() {
        return book_page;
    }

    public void setBook_page(book_Page book_page) {
        this.book_page = book_page;
    }
    public List<book_Page> getBook_pages() {
        return book_pages;
    }

    public void addBook_page(Book_page book_page) {
        this.book_pages.add(book_page);
    }

}