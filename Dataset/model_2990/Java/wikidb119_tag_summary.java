





import java.util.List;
import java.util.ArrayList;

public class wikidb119_tag_summary  {

    private String ts_tags;
    private String ts_rev_id;
    private String ts_rc_id;
    private String ts_log_id;



    public wikidb119_tag_summary(
        String ts_tags,        String ts_rev_id,        String ts_rc_id,        String ts_log_id    ) {
        this.ts_tags = ts_tags;
        this.ts_rev_id = ts_rev_id;
        this.ts_rc_id = ts_rc_id;
        this.ts_log_id = ts_log_id;
    }


    public String getTs_tags() {
        return ts_tags;
    }

    public void setTs_tags(String ts_tags) {
        this.ts_tags = ts_tags;
    }
    public String getTs_rev_id() {
        return ts_rev_id;
    }

    public void setTs_rev_id(String ts_rev_id) {
        this.ts_rev_id = ts_rev_id;
    }
    public String getTs_rc_id() {
        return ts_rc_id;
    }

    public void setTs_rc_id(String ts_rc_id) {
        this.ts_rc_id = ts_rc_id;
    }
    public String getTs_log_id() {
        return ts_log_id;
    }

    public void setTs_log_id(String ts_log_id) {
        this.ts_log_id = ts_log_id;
    }


}