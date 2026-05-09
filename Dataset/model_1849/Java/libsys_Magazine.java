





import java.util.List;
import java.util.ArrayList;

public class libsys_Magazine extends Medium {

    private String publisher;
    private String articles;



    public libsys_Magazine(
        String publisher,        String articles    ) {
        super(
        );
        this.publisher = publisher;
        this.articles = articles;
    }


    public String getPublisher() {
        return publisher;
    }

    public void setPublisher(String publisher) {
        this.publisher = publisher;
    }
    public String getArticles() {
        return articles;
    }

    public void setArticles(String articles) {
        this.articles = articles;
    }


}