





import java.util.List;
import java.util.ArrayList;

public class library_Book  {

    private int pages;
    private String category;
    private String title;



    public library_Book(
        int pages,        String category,        String title    ) {
        this.pages = pages;
        this.category = category;
        this.title = title;
    }


    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
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


}