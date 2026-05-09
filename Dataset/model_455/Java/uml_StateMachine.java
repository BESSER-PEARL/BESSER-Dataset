





import java.util.List;
import java.util.ArrayList;

public class uml_StateMachine extends Behavior {






    private uml_Region uml_region;




    private List<uml_State> uml_states;




    private List<uml_Region> uml_regions;




    private uml_State uml_state;




    private List<uml_StateMachine> uml_statemachines;


    public uml_StateMachine(
    ) {
        super(
        );
        this.uml_states = new ArrayList<>();
        this.uml_regions = new ArrayList<>();
        this.uml_statemachines = new ArrayList<>();
    }

    public uml_StateMachine(
        ArrayList<uml_State> uml_states,        ArrayList<uml_Region> uml_regions,        ArrayList<uml_StateMachine> uml_statemachines    ) {
        this.uml_states = uml_states;
        this.uml_regions = uml_regions;
        this.uml_statemachines = uml_statemachines;
    }


    public uml_Region getUml_region() {
        return uml_region;
    }

    public void setUml_region(uml_Region uml_region) {
        this.uml_region = uml_region;
    }
    public List<uml_State> getUml_states() {
        return uml_states;
    }

    public void addUml_state(Uml_state uml_state) {
        this.uml_states.add(uml_state);
    }
    public List<uml_Region> getUml_regions() {
        return uml_regions;
    }

    public void addUml_region(Uml_region uml_region) {
        this.uml_regions.add(uml_region);
    }
    public uml_State getUml_state() {
        return uml_state;
    }

    public void setUml_state(uml_State uml_state) {
        this.uml_state = uml_state;
    }
    public List<uml_StateMachine> getUml_statemachines() {
        return uml_statemachines;
    }

    public void addUml_statemachine(Uml_statemachine uml_statemachine) {
        this.uml_statemachines.add(uml_statemachine);
    }

}