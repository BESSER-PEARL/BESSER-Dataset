





import java.util.List;
import java.util.ArrayList;

public class cascadenotall_Book  {

    private String title;
    private String category;
    private String pages;



    public cascadenotall_Book(
        String title,        String category,        String pages    ) {
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
    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }


}