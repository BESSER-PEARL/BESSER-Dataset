





import java.util.List;
import java.util.ArrayList;

public class library_Book extends Identifiable {

    private String title;
    private int pages;
    private String category;



    public library_Book(
        String title,        int pages,        String category    ) {
        super(
        );
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


}