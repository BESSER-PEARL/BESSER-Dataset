





import java.util.List;
import java.util.ArrayList;

public class library_Book  {

    private String isbn;
    private String title;





    private library_Loan library_loan;




    private library_Library library_library;




    private library_Author library_author;


    public library_Book(
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

    public library_Loan getLibrary_loan() {
        return library_loan;
    }

    public void setLibrary_loan(library_Loan library_loan) {
        this.library_loan = library_loan;
    }
    public library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(library_Library library_library) {
        this.library_library = library_library;
    }
    public library_Author getLibrary_author() {
        return library_author;
    }

    public void setLibrary_author(library_Author library_author) {
        this.library_author = library_author;
    }

}