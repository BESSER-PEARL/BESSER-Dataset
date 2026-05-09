





import java.util.List;
import java.util.ArrayList;

public class efsm_Event  {

    private String return_;
    private String name;
    private String class_;





    private efsm_Transition efsm_transition;


    public efsm_Event(
        String return_,        String name,        String class_    ) {
        this.return_ = return_;
        this.name = name;
        this.class_ = class_;
    }


    public String getReturn_() {
        return return_;
    }

    public void setReturn_(String return_) {
        this.return_ = return_;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }

    public efsm_Transition getEfsm_transition() {
        return efsm_transition;
    }

    public void setEfsm_transition(efsm_Transition efsm_transition) {
        this.efsm_transition = efsm_transition;
    }

}