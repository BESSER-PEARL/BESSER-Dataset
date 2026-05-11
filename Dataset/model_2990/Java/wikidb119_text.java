





import java.util.List;
import java.util.ArrayList;

public class wikidb119_text  {

    private String old_id;
    private String old_text;
    private String old_flags;



    public wikidb119_text(
        String old_id,        String old_text,        String old_flags    ) {
        this.old_id = old_id;
        this.old_text = old_text;
        this.old_flags = old_flags;
    }


    public String getOld_id() {
        return old_id;
    }

    public void setOld_id(String old_id) {
        this.old_id = old_id;
    }
    public String getOld_text() {
        return old_text;
    }

    public void setOld_text(String old_text) {
        this.old_text = old_text;
    }
    public String getOld_flags() {
        return old_flags;
    }

    public void setOld_flags(String old_flags) {
        this.old_flags = old_flags;
    }


}