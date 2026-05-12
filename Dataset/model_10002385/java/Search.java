





import java.util.List;
import java.util.ArrayList;

public class Search  {

    private String bookTitle;
    private String authorName;
    private String priceLimit;



    public Search(
        String bookTitle,        String authorName,        String priceLimit    ) {
        this.bookTitle = bookTitle;
        this.authorName = authorName;
        this.priceLimit = priceLimit;
    }


    public String getBooktitle() {
        return bookTitle;
    }

    public void setBooktitle(String bookTitle) {
        this.bookTitle = bookTitle;
    }
    public String getAuthorname() {
        return authorName;
    }

    public void setAuthorname(String authorName) {
        this.authorName = authorName;
    }
    public String getPricelimit() {
        return priceLimit;
    }

    public void setPricelimit(String priceLimit) {
        this.priceLimit = priceLimit;
    }


}