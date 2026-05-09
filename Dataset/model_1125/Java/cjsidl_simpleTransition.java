





import java.util.List;
import java.util.ArrayList;

public class cjsidl_simpleTransition  {

    private String comment;





    private cjsidl_pushTransition cjsidl_pushtransition;




    private cjsidl_nextState cjsidl_nextstate;


    public cjsidl_simpleTransition(
        String comment    ) {
        this.comment = comment;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public cjsidl_pushTransition getCjsidl_pushtransition() {
        return cjsidl_pushtransition;
    }

    public void setCjsidl_pushtransition(cjsidl_pushTransition cjsidl_pushtransition) {
        this.cjsidl_pushtransition = cjsidl_pushtransition;
    }
    public cjsidl_nextState getCjsidl_nextstate() {
        return cjsidl_nextstate;
    }

    public void setCjsidl_nextstate(cjsidl_nextState cjsidl_nextstate) {
        this.cjsidl_nextstate = cjsidl_nextstate;
    }

}