





import java.util.List;
import java.util.ArrayList;

public class swml_WebPage  {

    private String title;
    private String relativeUrl;



    public swml_WebPage(
        String title,        String relativeUrl    ) {
        this.title = title;
        this.relativeUrl = relativeUrl;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getRelativeurl() {
        return relativeUrl;
    }

    public void setRelativeurl(String relativeUrl) {
        this.relativeUrl = relativeUrl;
    }


}