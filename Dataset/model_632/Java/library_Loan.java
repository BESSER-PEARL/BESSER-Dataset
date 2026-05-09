





import java.util.List;
import java.util.ArrayList;

public class library_Loan  {






    private library_Person library_person;




    private library_Library library_library;




    private library_Book library_book;


    public library_Loan(
    ) {
    }



    public library_Person getLibrary_person() {
        return library_person;
    }

    public void setLibrary_person(library_Person library_person) {
        this.library_person = library_person;
    }
    public library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(library_Library library_library) {
        this.library_library = library_library;
    }
    public library_Book getLibrary_book() {
        return library_book;
    }

    public void setLibrary_book(library_Book library_book) {
        this.library_book = library_book;
    }

}