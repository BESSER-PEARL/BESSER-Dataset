





import java.util.List;
import java.util.ArrayList;

public class cjsidl_popTransition  {

    private String comment;





    private cjsidl_transition cjsidl_transition;


    public cjsidl_popTransition(
        String comment    ) {
        this.comment = comment;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public cjsidl_transition getCjsidl_transition() {
        return cjsidl_transition;
    }

    public void setCjsidl_transition(cjsidl_transition cjsidl_transition) {
        this.cjsidl_transition = cjsidl_transition;
    }

}