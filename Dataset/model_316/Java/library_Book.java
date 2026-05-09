





import java.util.List;
import java.util.ArrayList;

public class library_Book  {

    private String pages;
    private String title;
    private String category;





    private library_Library library_library;


    public library_Book(
        String pages,        String title,        String category    ) {
        this.pages = pages;
        this.title = title;
        this.category = category;
    }


    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(library_Library library_library) {
        this.library_library = library_library;
    }

}