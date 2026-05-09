





import java.util.List;
import java.util.ArrayList;

public class library_Book extends CirculatingItem {

    private String title;
    private String category;
    private int pages;



    public library_Book(
        String title,        String category,        int pages    ) {
        super(
        );
        this.title = title;
        this.category = category;
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
    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
        this.pages = pages;
    }


}