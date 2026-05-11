





import java.util.List;
import java.util.ArrayList;

public class wikidb119_externallinks  {

    private String el_to;
    private String el_index;
    private String el_from;



    public wikidb119_externallinks(
        String el_to,        String el_index,        String el_from    ) {
        this.el_to = el_to;
        this.el_index = el_index;
        this.el_from = el_from;
    }


    public String getEl_to() {
        return el_to;
    }

    public void setEl_to(String el_to) {
        this.el_to = el_to;
    }
    public String getEl_index() {
        return el_index;
    }

    public void setEl_index(String el_index) {
        this.el_index = el_index;
    }
    public String getEl_from() {
        return el_from;
    }

    public void setEl_from(String el_from) {
        this.el_from = el_from;
    }


}