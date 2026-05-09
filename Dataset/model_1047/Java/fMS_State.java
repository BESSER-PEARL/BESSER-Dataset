





import java.util.List;
import java.util.ArrayList;

public class fMS_State  {

    private String name;





    private fMS_FSM fms_fsm;


    public fMS_State(
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

}