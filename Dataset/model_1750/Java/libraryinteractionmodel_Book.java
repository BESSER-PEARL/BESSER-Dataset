





import java.util.List;
import java.util.ArrayList;

public class libraryinteractionmodel_Book  {

    private String isbn;
    private String title;





    private libraryinteractionmodel_BookShort libraryinteractionmodel_bookshort;


    public libraryinteractionmodel_Book(
        String isbn,        String title    ) {
        this.isbn = isbn;
        this.title = title;
    }


    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public libraryinteractionmodel_BookShort getLibraryinteractionmodel_bookshort() {
        return libraryinteractionmodel_bookshort;
    }

    public void setLibraryinteractionmodel_bookshort(libraryinteractionmodel_BookShort libraryinteractionmodel_bookshort) {
        this.libraryinteractionmodel_bookshort = libraryinteractionmodel_bookshort;
    }

}