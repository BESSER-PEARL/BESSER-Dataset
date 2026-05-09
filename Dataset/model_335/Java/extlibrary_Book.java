





import java.util.List;
import java.util.ArrayList;

public class extlibrary_Book extends CirculatingItem {

    private String category;
    private String title;
    private int pages;



    public extlibrary_Book(
        String category,        String title,        int pages    ) {
        super(
        );
        this.category = category;
        this.title = title;
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
    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
        this.pages = pages;
    }


}