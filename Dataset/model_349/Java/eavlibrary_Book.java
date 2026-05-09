





import java.util.List;
import java.util.ArrayList;

public class eavlibrary_Book  {

    private String pages;
    private String title;
    private String category;
    private String test;



    public eavlibrary_Book(
        String pages,        String title,        String category,        String test    ) {
        this.pages = pages;
        this.title = title;
        this.category = category;
        this.test = test;
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
    public String getTest() {
        return test;
    }

    public void setTest(String test) {
        this.test = test;
    }


}