





import java.util.List;
import java.util.ArrayList;

public class cjsidl_state  {

    private String initial;
    private String comment;
    private String name;





    private cjsidl_startState cjsidl_startstate;




    private cjsidl_state cjsidl_state;




    private cjsidl_startState cjsidl_startstate;


    public cjsidl_state(
        String initial,        String comment,        String name    ) {
        this.initial = initial;
        this.comment = comment;
        this.name = name;
    }


    public String getInitial() {
        return initial;
    }

    public void setInitial(String initial) {
        this.initial = initial;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cjsidl_startState getCjsidl_startstate() {
        return cjsidl_startstate;
    }

    public void setCjsidl_startstate(cjsidl_startState cjsidl_startstate) {
        this.cjsidl_startstate = cjsidl_startstate;
    }
    public cjsidl_state getCjsidl_state() {
        return cjsidl_state;
    }

    public void setCjsidl_state(cjsidl_state cjsidl_state) {
        this.cjsidl_state = cjsidl_state;
    }
    public cjsidl_startState getCjsidl_startstate() {
        return cjsidl_startstate;
    }

    public void setCjsidl_startstate(cjsidl_startState cjsidl_startstate) {
        this.cjsidl_startstate = cjsidl_startstate;
    }

}