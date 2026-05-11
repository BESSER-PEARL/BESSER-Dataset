





import java.util.List;
import java.util.ArrayList;

public class wikidb119_pagelinks  {

    private String pl_title;
    private String pl_from;
    private String pl_namespace;



    public wikidb119_pagelinks(
        String pl_title,        String pl_from,        String pl_namespace    ) {
        this.pl_title = pl_title;
        this.pl_from = pl_from;
        this.pl_namespace = pl_namespace;
    }


    public String getPl_title() {
        return pl_title;
    }

    public void setPl_title(String pl_title) {
        this.pl_title = pl_title;
    }
    public String getPl_from() {
        return pl_from;
    }

    public void setPl_from(String pl_from) {
        this.pl_from = pl_from;
    }
    public String getPl_namespace() {
        return pl_namespace;
    }

    public void setPl_namespace(String pl_namespace) {
        this.pl_namespace = pl_namespace;
    }


}