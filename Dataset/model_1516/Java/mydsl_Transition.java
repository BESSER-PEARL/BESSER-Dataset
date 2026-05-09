





import java.util.List;
import java.util.ArrayList;

public class mydsl_Transition  {

    private String name;
    private String trigger;





    private List<mydsl_State> mydsl_states;




    private mydsl_FSM mydsl_fsm;


    public mydsl_Transition(
        String name,        String trigger    ) {
        this.name = name;
        this.trigger = trigger;
        this.mydsl_states = new ArrayList<>();
    }

    public mydsl_Transition(
        String name,        String trigger        ArrayList<mydsl_State> mydsl_states    ) {
        this.name = name;
        this.trigger = trigger;
        this.mydsl_states = mydsl_states;
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

    public List<mydsl_State> getMydsl_states() {
        return mydsl_states;
    }

    public void addMydsl_state(Mydsl_state mydsl_state) {
        this.mydsl_states.add(mydsl_state);
    }
    public mydsl_FSM getMydsl_fsm() {
        return mydsl_fsm;
    }

    public void setMydsl_fsm(mydsl_FSM mydsl_fsm) {
        this.mydsl_fsm = mydsl_fsm;
    }

}