





import java.util.List;
import java.util.ArrayList;

public class cjsidl_entry  {

    private String comment;





    private cjsidl_state cjsidl_state;


    public cjsidl_entry(
        String comment    ) {
        this.comment = comment;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public cjsidl_state getCjsidl_state() {
        return cjsidl_state;
    }

    public void setCjsidl_state(cjsidl_state cjsidl_state) {
        this.cjsidl_state = cjsidl_state;
    }

}