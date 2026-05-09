





import java.util.List;
import java.util.ArrayList;

public class sample_Transition  {

    private String name;
    private String trigger;





    private sample_State sample_state;




    private sample_State sample_state;




    private sample_FSM sample_fsm;


    public sample_Transition(
        String name,        String trigger    ) {
        this.name = name;
        this.trigger = trigger;
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

    public sample_State getSample_state() {
        return sample_state;
    }

    public void setSample_state(sample_State sample_state) {
        this.sample_state = sample_state;
    }
    public sample_State getSample_state() {
        return sample_state;
    }

    public void setSample_state(sample_State sample_state) {
        this.sample_state = sample_state;
    }
    public sample_FSM getSample_fsm() {
        return sample_fsm;
    }

    public void setSample_fsm(sample_FSM sample_fsm) {
        this.sample_fsm = sample_fsm;
    }

}