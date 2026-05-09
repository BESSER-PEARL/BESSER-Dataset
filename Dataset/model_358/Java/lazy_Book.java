





import java.util.List;
import java.util.ArrayList;

public class lazy_Book  {

    private String category;
    private String title;
    private String pages;





    private lazy_Library lazy_library;




    private lazy_Writer lazy_writer;




    private lazy_Writer lazy_writer;


    public lazy_Book(
        String category,        String title,        String pages    ) {
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
    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }

    public lazy_Library getLazy_library() {
        return lazy_library;
    }

    public void setLazy_library(lazy_Library lazy_library) {
        this.lazy_library = lazy_library;
    }
    public lazy_Writer getLazy_writer() {
        return lazy_writer;
    }

    public void setLazy_writer(lazy_Writer lazy_writer) {
        this.lazy_writer = lazy_writer;
    }
    public lazy_Writer getLazy_writer() {
        return lazy_writer;
    }

    public void setLazy_writer(lazy_Writer lazy_writer) {
        this.lazy_writer = lazy_writer;
    }

}