





import java.util.List;
import java.util.ArrayList;

public class dsl_State  {

    private String name;
    private boolean isFinal;





    private dsl_Transition dsl_transition;




    private dsl_Transition dsl_transition;




    private dsl_FSM dsl_fsm;


    public dsl_State(
        String name,        boolean isFinal    ) {
        this.name = name;
        this.isFinal = isFinal;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsfinal() {
        return isFinal;
    }

    public void setIsfinal(boolean isFinal) {
        this.isFinal = isFinal;
    }

    public dsl_Transition getDsl_transition() {
        return dsl_transition;
    }

    public void setDsl_transition(dsl_Transition dsl_transition) {
        this.dsl_transition = dsl_transition;
    }
    public dsl_Transition getDsl_transition() {
        return dsl_transition;
    }

    public void setDsl_transition(dsl_Transition dsl_transition) {
        this.dsl_transition = dsl_transition;
    }
    public dsl_FSM getDsl_fsm() {
        return dsl_fsm;
    }

    public void setDsl_fsm(dsl_FSM dsl_fsm) {
        this.dsl_fsm = dsl_fsm;
    }

}