





import java.util.List;
import java.util.ArrayList;

public class library_Book  {

    private String lastLocation;
    private String lastHref;
    private String author;
    private String lastOpened;
    private String bookURN;
    private String bookURL;
    private String collection;
    private String title;





    private library_Library library_library;


    public library_Book(
        String lastLocation,        String lastHref,        String author,        String lastOpened,        String bookURN,        String bookURL,        String collection,        String title    ) {
        this.lastLocation = lastLocation;
        this.lastHref = lastHref;
        this.author = author;
        this.lastOpened = lastOpened;
        this.bookURN = bookURN;
        this.bookURL = bookURL;
        this.collection = collection;
        this.title = title;
    }


    public String getLastlocation() {
        return lastLocation;
    }

    public void setLastlocation(String lastLocation) {
        this.lastLocation = lastLocation;
    }
    public String getLasthref() {
        return lastHref;
    }

    public void setLasthref(String lastHref) {
        this.lastHref = lastHref;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getLastopened() {
        return lastOpened;
    }

    public void setLastopened(String lastOpened) {
        this.lastOpened = lastOpened;
    }
    public String getBookurn() {
        return bookURN;
    }

    public void setBookurn(String bookURN) {
        this.bookURN = bookURN;
    }
    public String getBookurl() {
        return bookURL;
    }

    public void setBookurl(String bookURL) {
        this.bookURL = bookURL;
    }
    public String getCollection() {
        return collection;
    }

    public void setCollection(String collection) {
        this.collection = collection;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(library_Library library_library) {
        this.library_library = library_library;
    }

}