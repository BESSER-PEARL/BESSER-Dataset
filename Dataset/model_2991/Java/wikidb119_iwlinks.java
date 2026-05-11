





import java.util.List;
import java.util.ArrayList;

public class wikidb119_iwlinks  {

    private String iwl_title;
    private String iwl_prefix;
    private String iwl_from;



    public wikidb119_iwlinks(
        String iwl_title,        String iwl_prefix,        String iwl_from    ) {
        this.iwl_title = iwl_title;
        this.iwl_prefix = iwl_prefix;
        this.iwl_from = iwl_from;
    }


    public String getIwl_title() {
        return iwl_title;
    }

    public void setIwl_title(String iwl_title) {
        this.iwl_title = iwl_title;
    }
    public String getIwl_prefix() {
        return iwl_prefix;
    }

    public void setIwl_prefix(String iwl_prefix) {
        this.iwl_prefix = iwl_prefix;
    }
    public String getIwl_from() {
        return iwl_from;
    }

    public void setIwl_from(String iwl_from) {
        this.iwl_from = iwl_from;
    }


}