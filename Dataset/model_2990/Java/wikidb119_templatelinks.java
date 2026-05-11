





import java.util.List;
import java.util.ArrayList;

public class wikidb119_templatelinks  {

    private String tl_title;
    private String tl_namespace;
    private String tl_from;



    public wikidb119_templatelinks(
        String tl_title,        String tl_namespace,        String tl_from    ) {
        this.tl_title = tl_title;
        this.tl_namespace = tl_namespace;
        this.tl_from = tl_from;
    }


    public String getTl_title() {
        return tl_title;
    }

    public void setTl_title(String tl_title) {
        this.tl_title = tl_title;
    }
    public String getTl_namespace() {
        return tl_namespace;
    }

    public void setTl_namespace(String tl_namespace) {
        this.tl_namespace = tl_namespace;
    }
    public String getTl_from() {
        return tl_from;
    }

    public void setTl_from(String tl_from) {
        this.tl_from = tl_from;
    }


}