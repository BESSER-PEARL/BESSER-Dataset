





import java.util.List;
import java.util.ArrayList;

public class swml_WebPage  {

    private String relativeUrl;
    private String title;



    public swml_WebPage(
        String relativeUrl,        String title    ) {
        this.relativeUrl = relativeUrl;
        this.title = title;
    }


    public String getRelativeurl() {
        return relativeUrl;
    }

    public void setRelativeurl(String relativeUrl) {
        this.relativeUrl = relativeUrl;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}