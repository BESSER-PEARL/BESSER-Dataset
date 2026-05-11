





import java.util.List;
import java.util.ArrayList;

public class tfsm_State extends State {

    private int time;





    private tfsm_FSM tfsm_fsm;


    public tfsm_State(
        int time    ) {
        super(
        );
        this.time = time;
    }


    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }

    public tfsm_FSM getTfsm_fsm() {
        return tfsm_fsm;
    }

    public void setTfsm_fsm(tfsm_FSM tfsm_fsm) {
        this.tfsm_fsm = tfsm_fsm;
    }

}