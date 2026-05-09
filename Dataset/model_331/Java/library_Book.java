





import java.util.List;
import java.util.ArrayList;

public class library_Book  {

    private String title;
    private int pages;





    private library_Library library_library;


    public library_Book(
        String title,        int pages    ) {
        this.title = title;
        this.pages = pages;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
        this.pages = pages;
    }

    public library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(library_Library library_library) {
        this.library_library = library_library;
    }

}