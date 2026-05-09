





import java.util.List;
import java.util.ArrayList;

public class tfsm_Transition  {

    private String event;





    private tfsm_State tfsm_state;




    private tfsm_FSM tfsm_fsm;




    private tfsm_State tfsm_state;




    private List<tfsm_ClockReset> tfsm_clockresets;




    private tfsm_State tfsm_state;




    private tfsm_State tfsm_state;


    public tfsm_Transition(
        String event    ) {
        this.event = event;
        this.tfsm_clockresets = new ArrayList<>();
    }

    public tfsm_Transition(
        String event        ArrayList<tfsm_ClockReset> tfsm_clockresets    ) {
        this.event = event;
        this.tfsm_clockresets = tfsm_clockresets;
    }

    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }

    public tfsm_State getTfsm_state() {
        return tfsm_state;
    }

    public void setTfsm_state(tfsm_State tfsm_state) {
        this.tfsm_state = tfsm_state;
    }
    public tfsm_FSM getTfsm_fsm() {
        return tfsm_fsm;
    }

    public void setTfsm_fsm(tfsm_FSM tfsm_fsm) {
        this.tfsm_fsm = tfsm_fsm;
    }
    public tfsm_State getTfsm_state() {
        return tfsm_state;
    }

    public void setTfsm_state(tfsm_State tfsm_state) {
        this.tfsm_state = tfsm_state;
    }
    public List<tfsm_ClockReset> getTfsm_clockresets() {
        return tfsm_clockresets;
    }

    public void addTfsm_clockreset(Tfsm_clockreset tfsm_clockreset) {
        this.tfsm_clockresets.add(tfsm_clockreset);
    }
    public tfsm_State getTfsm_state() {
        return tfsm_state;
    }

    public void setTfsm_state(tfsm_State tfsm_state) {
        this.tfsm_state = tfsm_state;
    }
    public tfsm_State getTfsm_state() {
        return tfsm_state;
    }

    public void setTfsm_state(tfsm_State tfsm_state) {
        this.tfsm_state = tfsm_state;
    }

}