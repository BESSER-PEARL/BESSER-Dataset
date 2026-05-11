





import java.util.List;
import java.util.ArrayList;

public class article_ExternalArticle extends Article {

    private String url;



    public article_ExternalArticle(
        String url    ) {
        super(
        );
        this.url = url;
    }


    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }


}