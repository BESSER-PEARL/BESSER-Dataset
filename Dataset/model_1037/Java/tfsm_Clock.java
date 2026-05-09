





import java.util.List;
import java.util.ArrayList;

public class tfsm_Clock  {

    private int tick;
    private String name;





    private tfsm_FSM tfsm_fsm;




    private tfsm_ClockReset tfsm_clockreset;


    public tfsm_Clock(
        int tick,        String name    ) {
        this.tick = tick;
        this.name = name;
    }


    public int getTick() {
        return tick;
    }

    public void setTick(int tick) {
        this.tick = tick;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tfsm_FSM getTfsm_fsm() {
        return tfsm_fsm;
    }

    public void setTfsm_fsm(tfsm_FSM tfsm_fsm) {
        this.tfsm_fsm = tfsm_fsm;
    }
    public tfsm_ClockReset getTfsm_clockreset() {
        return tfsm_clockreset;
    }

    public void setTfsm_clockreset(tfsm_ClockReset tfsm_clockreset) {
        this.tfsm_clockreset = tfsm_clockreset;
    }

}