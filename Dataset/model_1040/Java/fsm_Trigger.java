





import java.util.List;
import java.util.ArrayList;

public class fsm_Trigger  {

    private String expression;





    private fsm_Transition fsm_transition;




    private fsm_OrTrigger fsm_ortrigger;




    private fsm_AndTrigger fsm_andtrigger;




    private fsm_NotTrigger fsm_nottrigger;




    private fsm_OrTrigger fsm_ortrigger;




    private fsm_AndTrigger fsm_andtrigger;


    public fsm_Trigger(
        String expression    ) {
        this.expression = expression;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public fsm_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(fsm_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }
    public fsm_OrTrigger getFsm_ortrigger() {
        return fsm_ortrigger;
    }

    public void setFsm_ortrigger(fsm_OrTrigger fsm_ortrigger) {
        this.fsm_ortrigger = fsm_ortrigger;
    }
    public fsm_AndTrigger getFsm_andtrigger() {
        return fsm_andtrigger;
    }

    public void setFsm_andtrigger(fsm_AndTrigger fsm_andtrigger) {
        this.fsm_andtrigger = fsm_andtrigger;
    }
    public fsm_NotTrigger getFsm_nottrigger() {
        return fsm_nottrigger;
    }

    public void setFsm_nottrigger(fsm_NotTrigger fsm_nottrigger) {
        this.fsm_nottrigger = fsm_nottrigger;
    }
    public fsm_OrTrigger getFsm_ortrigger() {
        return fsm_ortrigger;
    }

    public void setFsm_ortrigger(fsm_OrTrigger fsm_ortrigger) {
        this.fsm_ortrigger = fsm_ortrigger;
    }
    public fsm_AndTrigger getFsm_andtrigger() {
        return fsm_andtrigger;
    }

    public void setFsm_andtrigger(fsm_AndTrigger fsm_andtrigger) {
        this.fsm_andtrigger = fsm_andtrigger;
    }

}