





import java.util.List;
import java.util.ArrayList;

public class cjsidl_defaultTransition  {

    private String type;
    private String comment;





    private cjsidl_state cjsidl_state;




    private cjsidl_EObject cjsidl_eobject;




    private cjsidl_defaultState cjsidl_defaultstate;




    private cjsidl_guard cjsidl_guard;


    public cjsidl_defaultTransition(
        String type,        String comment    ) {
        this.type = type;
        this.comment = comment;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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
    public cjsidl_EObject getCjsidl_eobject() {
        return cjsidl_eobject;
    }

    public void setCjsidl_eobject(cjsidl_EObject cjsidl_eobject) {
        this.cjsidl_eobject = cjsidl_eobject;
    }
    public cjsidl_defaultState getCjsidl_defaultstate() {
        return cjsidl_defaultstate;
    }

    public void setCjsidl_defaultstate(cjsidl_defaultState cjsidl_defaultstate) {
        this.cjsidl_defaultstate = cjsidl_defaultstate;
    }
    public cjsidl_guard getCjsidl_guard() {
        return cjsidl_guard;
    }

    public void setCjsidl_guard(cjsidl_guard cjsidl_guard) {
        this.cjsidl_guard = cjsidl_guard;
    }

}