





import java.util.List;
import java.util.ArrayList;

public class extlibraryprofile_Book extends CirculatingItem {

    private String category;
    private String pages;



    public extlibraryprofile_Book(
        String category,        String pages    ) {
        super(
        );
        this.category = category;
        this.pages = pages;
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