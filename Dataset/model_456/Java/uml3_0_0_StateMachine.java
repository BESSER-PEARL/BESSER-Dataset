





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_StateMachine extends Behavior {






    private uml3_0_0_Region uml3_0_0_region;




    private List<uml3_0_0_State> uml3_0_0_states;




    private List<uml3_0_0_Region> uml3_0_0_regions;




    private uml3_0_0_StateMachine uml3_0_0_statemachine;




    private uml3_0_0_State uml3_0_0_state;


    public uml3_0_0_StateMachine(
    ) {
        super(
        );
        this.uml3_0_0_states = new ArrayList<>();
        this.uml3_0_0_regions = new ArrayList<>();
    }

    public uml3_0_0_StateMachine(
        ArrayList<uml3_0_0_State> uml3_0_0_states,        ArrayList<uml3_0_0_Region> uml3_0_0_regions    ) {
        this.uml3_0_0_states = uml3_0_0_states;
        this.uml3_0_0_regions = uml3_0_0_regions;
    }


    public uml3_0_0_Region getUml3_0_0_region() {
        return uml3_0_0_region;
    }

    public void setUml3_0_0_region(uml3_0_0_Region uml3_0_0_region) {
        this.uml3_0_0_region = uml3_0_0_region;
    }
    public List<uml3_0_0_State> getUml3_0_0_states() {
        return uml3_0_0_states;
    }

    public void addUml3_0_0_state(Uml3_0_0_state uml3_0_0_state) {
        this.uml3_0_0_states.add(uml3_0_0_state);
    }
    public List<uml3_0_0_Region> getUml3_0_0_regions() {
        return uml3_0_0_regions;
    }

    public void addUml3_0_0_region(Uml3_0_0_region uml3_0_0_region) {
        this.uml3_0_0_regions.add(uml3_0_0_region);
    }
    public uml3_0_0_StateMachine getUml3_0_0_statemachine() {
        return uml3_0_0_statemachine;
    }

    public void setUml3_0_0_statemachine(uml3_0_0_StateMachine uml3_0_0_statemachine) {
        this.uml3_0_0_statemachine = uml3_0_0_statemachine;
    }
    public uml3_0_0_State getUml3_0_0_state() {
        return uml3_0_0_state;
    }

    public void setUml3_0_0_state(uml3_0_0_State uml3_0_0_state) {
        this.uml3_0_0_state = uml3_0_0_state;
    }

}