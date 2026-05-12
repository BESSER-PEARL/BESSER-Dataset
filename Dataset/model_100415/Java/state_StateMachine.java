





import java.util.List;
import java.util.ArrayList;

public class state_StateMachine extends NamedElement {






    private state_Region state_region;




    private List<state_Region> state_regions;


    public state_StateMachine(
    ) {
        super(
        );
        this.state_regions = new ArrayList<>();
    }

    public state_StateMachine(
        ArrayList<state_Region> state_regions    ) {
        this.state_regions = state_regions;
    }


    public state_Region getState_region() {
        return state_region;
    }

    public void setState_region(state_Region state_region) {
        this.state_region = state_region;
    }
    public List<state_Region> getState_regions() {
        return state_regions;
    }

    public void addState_region(State_region state_region) {
        this.state_regions.add(state_region);
    }

}