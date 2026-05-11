





import java.util.List;
import java.util.ArrayList;

public class wikidb116_version116_change_tag  {

    private String ct_rc_id;
    private String ct_tag;
    private String ct_log_id;
    private String ct_rev_id;
    private String ct_params;



    public wikidb116_version116_change_tag(
        String ct_rc_id,        String ct_tag,        String ct_log_id,        String ct_rev_id,        String ct_params    ) {
        this.ct_rc_id = ct_rc_id;
        this.ct_tag = ct_tag;
        this.ct_log_id = ct_log_id;
        this.ct_rev_id = ct_rev_id;
        this.ct_params = ct_params;
    }


    public String getCt_rc_id() {
        return ct_rc_id;
    }

    public void setCt_rc_id(String ct_rc_id) {
        this.ct_rc_id = ct_rc_id;
    }
    public String getCt_tag() {
        return ct_tag;
    }

    public void setCt_tag(String ct_tag) {
        this.ct_tag = ct_tag;
    }
    public String getCt_log_id() {
        return ct_log_id;
    }

    public void setCt_log_id(String ct_log_id) {
        this.ct_log_id = ct_log_id;
    }
    public String getCt_rev_id() {
        return ct_rev_id;
    }

    public void setCt_rev_id(String ct_rev_id) {
        this.ct_rev_id = ct_rev_id;
    }
    public String getCt_params() {
        return ct_params;
    }

    public void setCt_params(String ct_params) {
        this.ct_params = ct_params;
    }


}