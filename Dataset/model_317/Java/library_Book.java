





import java.util.List;
import java.util.ArrayList;

public class library_Book  {

    private String title;
    private String pages;
    private String category;



    public library_Book(
        String title,        String pages,        String category    ) {
        this.title = title;
        this.pages = pages;
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
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }


}