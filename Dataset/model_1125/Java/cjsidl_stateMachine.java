





import java.util.List;
import java.util.ArrayList;

public class cjsidl_stateMachine  {

    private String comment;
    private String name;





    private cjsidl_startState cjsidl_startstate;




    private List<cjsidl_state> cjsidl_states;




    private List<cjsidl_refAttr> cjsidl_refattrs;




    private cjsidl_defaultState cjsidl_defaultstate;




    private cjsidl_protocolBehavior cjsidl_protocolbehavior;


    public cjsidl_stateMachine(
        String comment,        String name    ) {
        this.comment = comment;
        this.name = name;
        this.cjsidl_states = new ArrayList<>();
        this.cjsidl_refattrs = new ArrayList<>();
    }

    public cjsidl_stateMachine(
        String comment,        String name        ArrayList<cjsidl_state> cjsidl_states,        ArrayList<cjsidl_refAttr> cjsidl_refattrs    ) {
        this.comment = comment;
        this.name = name;
        this.cjsidl_states = cjsidl_states;
        this.cjsidl_refattrs = cjsidl_refattrs;
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
    public List<cjsidl_state> getCjsidl_states() {
        return cjsidl_states;
    }

    public void addCjsidl_state(Cjsidl_state cjsidl_state) {
        this.cjsidl_states.add(cjsidl_state);
    }
    public List<cjsidl_refAttr> getCjsidl_refattrs() {
        return cjsidl_refattrs;
    }

    public void addCjsidl_refattr(Cjsidl_refattr cjsidl_refattr) {
        this.cjsidl_refattrs.add(cjsidl_refattr);
    }
    public cjsidl_defaultState getCjsidl_defaultstate() {
        return cjsidl_defaultstate;
    }

    public void setCjsidl_defaultstate(cjsidl_defaultState cjsidl_defaultstate) {
        this.cjsidl_defaultstate = cjsidl_defaultstate;
    }
    public cjsidl_protocolBehavior getCjsidl_protocolbehavior() {
        return cjsidl_protocolbehavior;
    }

    public void setCjsidl_protocolbehavior(cjsidl_protocolBehavior cjsidl_protocolbehavior) {
        this.cjsidl_protocolbehavior = cjsidl_protocolbehavior;
    }

}