





import java.util.List;
import java.util.ArrayList;

public class eavlibrary_Book  {

    private String category;
    private String pages;
    private String test;
    private String title;





    private eavlibrary_Library eavlibrary_library;


    public eavlibrary_Book(
        String category,        String pages,        String test,        String title    ) {
        this.category = category;
        this.pages = pages;
        this.test = test;
        this.title = title;
    }


    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }
    public String getTest() {
        return test;
    }

    public void setTest(String test) {
        this.test = test;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public eavlibrary_Library getEavlibrary_library() {
        return eavlibrary_library;
    }

    public void setEavlibrary_library(eavlibrary_Library eavlibrary_library) {
        this.eavlibrary_library = eavlibrary_library;
    }

}