





import java.util.List;
import java.util.ArrayList;

public class libraryinteractionmodel_BookShort  {

    private String title;
    private String isbn;





    private libraryinteractionmodel_Books libraryinteractionmodel_books;




    private libraryinteractionmodel_Book libraryinteractionmodel_book;


    public libraryinteractionmodel_BookShort(
        String title,        String isbn    ) {
        this.title = title;
        this.isbn = isbn;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }

    public libraryinteractionmodel_Books getLibraryinteractionmodel_books() {
        return libraryinteractionmodel_books;
    }

    public void setLibraryinteractionmodel_books(libraryinteractionmodel_Books libraryinteractionmodel_books) {
        this.libraryinteractionmodel_books = libraryinteractionmodel_books;
    }
    public libraryinteractionmodel_Book getLibraryinteractionmodel_book() {
        return libraryinteractionmodel_book;
    }

    public void setLibraryinteractionmodel_book(libraryinteractionmodel_Book libraryinteractionmodel_book) {
        this.libraryinteractionmodel_book = libraryinteractionmodel_book;
    }

}