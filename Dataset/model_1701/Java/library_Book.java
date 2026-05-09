





import java.util.List;
import java.util.ArrayList;

public class library_Book  {

    private String title;





    private library_Library library_library;




    private library_Book library_book;


    public library_Book(
        String title    ) {
        this.title = title;
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
    public library_Book getLibrary_book() {
        return library_book;
    }

    public void setLibrary_book(library_Book library_book) {
        this.library_book = library_book;
    }

}