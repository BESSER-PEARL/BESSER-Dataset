





import java.util.List;
import java.util.ArrayList;

public class article_ExternalTarget extends LinkTarget {

    private String url;



    public article_ExternalTarget(
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