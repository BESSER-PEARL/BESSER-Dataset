





import java.util.List;
import java.util.ArrayList;

public class libraryExample_Book  {

    private String category;
    private String title;
    private int pages;





    private libraryExample_Library libraryexample_library;


    public libraryExample_Book(
        String category,        String title,        int pages    ) {
        this.category = category;
        this.title = title;
        this.pages = pages;
    }


    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
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

    public libraryExample_Library getLibraryexample_library() {
        return libraryexample_library;
    }

    public void setLibraryexample_library(libraryExample_Library libraryexample_library) {
        this.libraryexample_library = libraryexample_library;
    }

}