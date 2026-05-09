





import java.util.List;
import java.util.ArrayList;

public class library_Book  {

    private String ISBN;
    private String pages;
    private String title;



    public library_Book(
        String ISBN,        String pages,        String title    ) {
        this.ISBN = ISBN;
        this.pages = pages;
        this.title = title;
    }


    public String getIsbn() {
        return ISBN;
    }

    public void setIsbn(String ISBN) {
        this.ISBN = ISBN;
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