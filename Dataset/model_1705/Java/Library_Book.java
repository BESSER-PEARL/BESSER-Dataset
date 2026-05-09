





import java.util.List;
import java.util.ArrayList;

public class Library_Book  {

    private int pages;
    private String title;





    private Library_Writer library_writer;


    public Library_Book(
        int pages,        String title    ) {
        this.pages = pages;
        this.title = title;
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

    public Library_Writer getLibrary_writer() {
        return library_writer;
    }

    public void setLibrary_writer(Library_Writer library_writer) {
        this.library_writer = library_writer;
    }

}