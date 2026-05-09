





import java.util.List;
import java.util.ArrayList;

public class extlibrary_Book  {

    private String title;
    private int pages;



    public extlibrary_Book(
        String title,        int pages    ) {
        this.title = title;
        this.pages = pages;
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