





import java.util.List;
import java.util.ArrayList;

public class model_Transition  {

    private String action;
    private String name;
    private String trigger;





    private model_FSM model_fsm;




    private model_FSM model_fsm;


    public model_Transition(
        String action,        String name,        String trigger    ) {
        this.action = action;
        this.name = name;
        this.trigger = trigger;
    }


    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTrigger() {
        return trigger;
    }

    public void setTrigger(String trigger) {
        this.trigger = trigger;
    }

    public model_FSM getModel_fsm() {
        return model_fsm;
    }

    public void setModel_fsm(model_FSM model_fsm) {
        this.model_fsm = model_fsm;
    }
    public model_FSM getModel_fsm() {
        return model_fsm;
    }

    public void setModel_fsm(model_FSM model_fsm) {
        this.model_fsm = model_fsm;
    }

}