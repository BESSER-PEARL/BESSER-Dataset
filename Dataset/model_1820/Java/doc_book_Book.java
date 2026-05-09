





import java.util.List;
import java.util.ArrayList;

public class doc_book_Book extends BookContainer {

    private String title;
    private String copyrightText;
    private String version;
    private String copyrightMarker;





    private List<Author> authors;


    public doc_book_Book(
        String title,        String copyrightText,        String version,        String copyrightMarker    ) {
        super(
        );
        this.title = title;
        this.copyrightText = copyrightText;
        this.version = version;
        this.copyrightMarker = copyrightMarker;
        this.authors = new ArrayList<>();
    }

    public doc_book_Book(
        String title,        String copyrightText,        String version,        String copyrightMarker        ArrayList<Author> authors    ) {
        this.title = title;
        this.copyrightText = copyrightText;
        this.version = version;
        this.copyrightMarker = copyrightMarker;
        this.authors = authors;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getCopyrighttext() {
        return copyrightText;
    }

    public void setCopyrighttext(String copyrightText) {
        this.copyrightText = copyrightText;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getCopyrightmarker() {
        return copyrightMarker;
    }

    public void setCopyrightmarker(String copyrightMarker) {
        this.copyrightMarker = copyrightMarker;
    }

    public List<Author> getAuthors() {
        return authors;
    }

    public void addAuthor(Author author) {
        this.authors.add(author);
    }

}