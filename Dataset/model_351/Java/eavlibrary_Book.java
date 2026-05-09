





import java.util.List;
import java.util.ArrayList;

public class eavlibrary_Book  {

    private String pages;
    private String category;
    private String test;
    private String title;



    public eavlibrary_Book(
        String pages,        String category,        String test,        String title    ) {
        this.pages = pages;
        this.category = category;
        this.test = test;
        this.title = title;
    }


    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
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


}