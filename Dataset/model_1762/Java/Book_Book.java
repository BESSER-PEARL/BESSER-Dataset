





import java.util.List;
import java.util.ArrayList;

public class Book_Book  {

    private String name;
    private int nbpages;
    private String isbn;





    private Book_Library book_library;


    public Book_Book(
        String name,        int nbpages,        String isbn    ) {
        this.name = name;
        this.nbpages = nbpages;
        this.isbn = isbn;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getNbpages() {
        return nbpages;
    }

    public void setNbpages(int nbpages) {
        this.nbpages = nbpages;
    }
    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }

    public Book_Library getBook_library() {
        return book_library;
    }

    public void setBook_library(Book_Library book_library) {
        this.book_library = book_library;
    }

}