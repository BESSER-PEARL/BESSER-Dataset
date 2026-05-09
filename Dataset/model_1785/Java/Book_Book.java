





import java.util.List;
import java.util.ArrayList;

public class Book_Book  {

    private String title;
    private String authorName;



    public Book_Book(
        String title,        String authorName    ) {
        this.title = title;
        this.authorName = authorName;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getAuthorname() {
        return authorName;
    }

    public void setAuthorname(String authorName) {
        this.authorName = authorName;
    }


}