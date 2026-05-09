





import java.util.List;
import java.util.ArrayList;

public class library_Book  {

    private int pages;
    private String title;
    private String category;



    public library_Book(
        int pages,        String title,        String category    ) {
        this.pages = pages;
        this.title = title;
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
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }


}