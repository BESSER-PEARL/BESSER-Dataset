





import java.util.List;
import java.util.ArrayList;

public class eiqlibrary_Book  {

    private String category;
    private int pages;
    private String title;



    public eiqlibrary_Book(
        String category,        int pages,        String title    ) {
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


}