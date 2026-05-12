





import java.util.List;
import java.util.ArrayList;

public class Library_Patron  {

    private String books;
    private int maxBookCheckOut;





    private Library library;


    public Library_Patron(
        String books,        int maxBookCheckOut    ) {
        this.books = books;
        this.maxBookCheckOut = maxBookCheckOut;
    }


    public String getBooks() {
        return books;
    }

    public void setBooks(String books) {
        this.books = books;
    }
    public int getMaxbookcheckout() {
        return maxBookCheckOut;
    }

    public void setMaxbookcheckout(int maxBookCheckOut) {
        this.maxBookCheckOut = maxBookCheckOut;
    }

    public Library getLibrary() {
        return library;
    }

    public void setLibrary(Library library) {
        this.library = library;
    }

}