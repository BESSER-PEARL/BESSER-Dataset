





import java.util.List;
import java.util.ArrayList;

public class news  {

    private String dlnews;
    private String author;



    public news(
        String dlnews,        String author    ) {
        this.dlnews = dlnews;
        this.author = author;
    }


    public String getDlnews() {
        return dlnews;
    }

    public void setDlnews(String dlnews) {
        this.dlnews = dlnews;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }


}