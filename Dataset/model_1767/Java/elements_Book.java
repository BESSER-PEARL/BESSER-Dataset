





import java.util.List;
import java.util.ArrayList;

public class elements_Book  {

    private String category;
    private String uuid;
    private String pages;
    private String title;



    public elements_Book(
        String category,        String uuid,        String pages,        String title    ) {
        this.category = category;
        this.uuid = uuid;
        this.pages = pages;
        this.title = title;
    }


    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public String getUuid() {
        return uuid;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid;
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