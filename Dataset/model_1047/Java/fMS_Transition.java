





import java.util.List;
import java.util.ArrayList;

public class fMS_Transition  {

    private String name;





    private fMS_FSM fms_fsm;




    private fMS_State fms_state;




    private fMS_State fms_state;


    public fMS_Transition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fMS_FSM getFms_fsm() {
        return fms_fsm;
    }

    public void setFms_fsm(fMS_FSM fms_fsm) {
        this.fms_fsm = fms_fsm;
    }
    public fMS_State getFms_state() {
        return fms_state;
    }

    public void setFms_state(fMS_State fms_state) {
        this.fms_state = fms_state;
    }
    public fMS_State getFms_state() {
        return fms_state;
    }

    public void setFms_state(fMS_State fms_state) {
        this.fms_state = fms_state;
    }

}