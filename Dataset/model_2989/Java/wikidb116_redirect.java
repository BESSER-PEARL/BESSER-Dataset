





import java.util.List;
import java.util.ArrayList;

public class wikidb116_redirect  {

    private String rd_from;
    private String rd_interwiki;
    private String rd_fragment;
    private String rd_namespace;
    private String rd_title;



    public wikidb116_redirect(
        String rd_from,        String rd_interwiki,        String rd_fragment,        String rd_namespace,        String rd_title    ) {
        this.rd_from = rd_from;
        this.rd_interwiki = rd_interwiki;
        this.rd_fragment = rd_fragment;
        this.rd_namespace = rd_namespace;
        this.rd_title = rd_title;
    }


    public String getRd_from() {
        return rd_from;
    }

    public void setRd_from(String rd_from) {
        this.rd_from = rd_from;
    }
    public String getRd_interwiki() {
        return rd_interwiki;
    }

    public void setRd_interwiki(String rd_interwiki) {
        this.rd_interwiki = rd_interwiki;
    }
    public String getRd_fragment() {
        return rd_fragment;
    }

    public void setRd_fragment(String rd_fragment) {
        this.rd_fragment = rd_fragment;
    }
    public String getRd_namespace() {
        return rd_namespace;
    }

    public void setRd_namespace(String rd_namespace) {
        this.rd_namespace = rd_namespace;
    }
    public String getRd_title() {
        return rd_title;
    }

    public void setRd_title(String rd_title) {
        this.rd_title = rd_title;
    }


}