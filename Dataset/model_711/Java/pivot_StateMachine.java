





import java.util.List;
import java.util.ArrayList;

public class pivot_StateMachine extends Behavior {






    private List<pivot_Region> pivot_regions;




    private pivot_Region pivot_region;




    private pivot_StateMachine pivot_statemachine;




    private List<pivot_Pseudostate> pivot_pseudostates;




    private List<pivot_State> pivot_states;




    private pivot_State pivot_state;




    private pivot_Pseudostate pivot_pseudostate;


    public pivot_StateMachine(
    ) {
        super(
        );
        this.pivot_regions = new ArrayList<>();
        this.pivot_pseudostates = new ArrayList<>();
        this.pivot_states = new ArrayList<>();
    }

    public pivot_StateMachine(
        ArrayList<pivot_Region> pivot_regions,        ArrayList<pivot_Pseudostate> pivot_pseudostates,        ArrayList<pivot_State> pivot_states    ) {
        this.pivot_regions = pivot_regions;
        this.pivot_pseudostates = pivot_pseudostates;
        this.pivot_states = pivot_states;
    }


    public List<pivot_Region> getPivot_regions() {
        return pivot_regions;
    }

    public void addPivot_region(Pivot_region pivot_region) {
        this.pivot_regions.add(pivot_region);
    }
    public pivot_Region getPivot_region() {
        return pivot_region;
    }

    public void setPivot_region(pivot_Region pivot_region) {
        this.pivot_region = pivot_region;
    }
    public pivot_StateMachine getPivot_statemachine() {
        return pivot_statemachine;
    }

    public void setPivot_statemachine(pivot_StateMachine pivot_statemachine) {
        this.pivot_statemachine = pivot_statemachine;
    }
    public List<pivot_Pseudostate> getPivot_pseudostates() {
        return pivot_pseudostates;
    }

    public void addPivot_pseudostate(Pivot_pseudostate pivot_pseudostate) {
        this.pivot_pseudostates.add(pivot_pseudostate);
    }
    public List<pivot_State> getPivot_states() {
        return pivot_states;
    }

    public void addPivot_state(Pivot_state pivot_state) {
        this.pivot_states.add(pivot_state);
    }
    public pivot_State getPivot_state() {
        return pivot_state;
    }

    public void setPivot_state(pivot_State pivot_state) {
        this.pivot_state = pivot_state;
    }
    public pivot_Pseudostate getPivot_pseudostate() {
        return pivot_pseudostate;
    }

    public void setPivot_pseudostate(pivot_Pseudostate pivot_pseudostate) {
        this.pivot_pseudostate = pivot_pseudostate;
    }

}