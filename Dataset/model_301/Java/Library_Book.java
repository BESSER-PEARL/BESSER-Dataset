





import java.util.List;
import java.util.ArrayList;

public class Library_Book extends CirculatingItem {

    private int pages;
    private String title;
    private String category;





    private Library_Writer library_writer;




    private Library_Library library_library;




    private Library_Writer library_writer;


    public Library_Book(
        int pages,        String title,        String category    ) {
        super(
        );
        this.pages = pages;
        this.title = title;
        this.category = category;
    }


    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
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

    public Library_Writer getLibrary_writer() {
        return library_writer;
    }

    public void setLibrary_writer(Library_Writer library_writer) {
        this.library_writer = library_writer;
    }
    public Library_Library getLibrary_library() {
        return library_library;
    }

    public void setLibrary_library(Library_Library library_library) {
        this.library_library = library_library;
    }
    public Library_Writer getLibrary_writer() {
        return library_writer;
    }

    public void setLibrary_writer(Library_Writer library_writer) {
        this.library_writer = library_writer;
    }

}