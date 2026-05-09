





import java.util.List;
import java.util.ArrayList;

public class bookstore_Magazine extends Ent {

    private String version;
    private int pages;
    private String title;





    private bookstore_Person bookstore_person;


    public bookstore_Magazine(
        String version,        int pages,        String title    ) {
        super(
        );
        this.version = version;
        this.pages = pages;
        this.title = title;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
        this.pages = pages;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public bookstore_Person getBookstore_person() {
        return bookstore_person;
    }

    public void setBookstore_person(bookstore_Person bookstore_person) {
        this.bookstore_person = bookstore_person;
    }

}