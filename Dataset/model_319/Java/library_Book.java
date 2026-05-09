





import java.util.List;
import java.util.ArrayList;

public class library_Book  {

    private String category;
    private String pages;
    private String title;



    public library_Book(
        String category,        String pages,        String title    ) {
        this.category = category;
        this.pages = pages;
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
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}