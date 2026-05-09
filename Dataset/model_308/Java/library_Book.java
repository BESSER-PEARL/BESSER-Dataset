





import java.util.List;
import java.util.ArrayList;

public class library_Book  {

    private String category;
    private String title;
    private String test;
    private String pages;



    public library_Book(
        String category,        String title,        String test,        String pages    ) {
        this.category = category;
        this.title = title;
        this.test = test;
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
    public String getTest() {
        return test;
    }

    public void setTest(String test) {
        this.test = test;
    }
    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }


}