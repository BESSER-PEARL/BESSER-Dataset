





import java.util.List;
import java.util.ArrayList;

public class wikidb116_page_props  {

    private String pp_propname;
    private String pp_value;
    private String pp_page;



    public wikidb116_page_props(
        String pp_propname,        String pp_value,        String pp_page    ) {
        this.pp_propname = pp_propname;
        this.pp_value = pp_value;
        this.pp_page = pp_page;
    }


    public String getPp_propname() {
        return pp_propname;
    }

    public void setPp_propname(String pp_propname) {
        this.pp_propname = pp_propname;
    }
    public String getPp_value() {
        return pp_value;
    }

    public void setPp_value(String pp_value) {
        this.pp_value = pp_value;
    }
    public String getPp_page() {
        return pp_page;
    }

    public void setPp_page(String pp_page) {
        this.pp_page = pp_page;
    }


}