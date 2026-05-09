





import java.util.List;
import java.util.ArrayList;

public class cjsidl_pushTransition  {

    private String comment;





    private cjsidl_nextState cjsidl_nextstate;


    public cjsidl_pushTransition(
        String comment    ) {
        this.comment = comment;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public cjsidl_nextState getCjsidl_nextstate() {
        return cjsidl_nextstate;
    }

    public void setCjsidl_nextstate(cjsidl_nextState cjsidl_nextstate) {
        this.cjsidl_nextstate = cjsidl_nextstate;
    }

}