





import java.util.List;
import java.util.ArrayList;

public class wikidb116_log_search  {

    private String ls_field;
    private String ls_log_id;
    private String ls_value;



    public wikidb116_log_search(
        String ls_field,        String ls_log_id,        String ls_value    ) {
        this.ls_field = ls_field;
        this.ls_log_id = ls_log_id;
        this.ls_value = ls_value;
    }


    public String getLs_field() {
        return ls_field;
    }

    public void setLs_field(String ls_field) {
        this.ls_field = ls_field;
    }
    public String getLs_log_id() {
        return ls_log_id;
    }

    public void setLs_log_id(String ls_log_id) {
        this.ls_log_id = ls_log_id;
    }
    public String getLs_value() {
        return ls_value;
    }

    public void setLs_value(String ls_value) {
        this.ls_value = ls_value;
    }


}