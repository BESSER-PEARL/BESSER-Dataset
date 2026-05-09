





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_StateMachine extends Behavior {






    private CompleteDSLPckg_Region completedslpckg_region;




    private List<CompleteDSLPckg_State> completedslpckg_states;




    private CompleteDSLPckg_StateMachine completedslpckg_statemachine;




    private List<CompleteDSLPckg_Region> completedslpckg_regions;




    private CompleteDSLPckg_State completedslpckg_state;


    public CompleteDSLPckg_StateMachine(
    ) {
        super(
        );
        this.completedslpckg_states = new ArrayList<>();
        this.completedslpckg_regions = new ArrayList<>();
    }

    public CompleteDSLPckg_StateMachine(
        ArrayList<CompleteDSLPckg_State> completedslpckg_states,        ArrayList<CompleteDSLPckg_Region> completedslpckg_regions    ) {
        this.completedslpckg_states = completedslpckg_states;
        this.completedslpckg_regions = completedslpckg_regions;
    }


    public CompleteDSLPckg_Region getCompletedslpckg_region() {
        return completedslpckg_region;
    }

    public void setCompletedslpckg_region(CompleteDSLPckg_Region completedslpckg_region) {
        this.completedslpckg_region = completedslpckg_region;
    }
    public List<CompleteDSLPckg_State> getCompletedslpckg_states() {
        return completedslpckg_states;
    }

    public void addCompletedslpckg_state(Completedslpckg_state completedslpckg_state) {
        this.completedslpckg_states.add(completedslpckg_state);
    }
    public CompleteDSLPckg_StateMachine getCompletedslpckg_statemachine() {
        return completedslpckg_statemachine;
    }

    public void setCompletedslpckg_statemachine(CompleteDSLPckg_StateMachine completedslpckg_statemachine) {
        this.completedslpckg_statemachine = completedslpckg_statemachine;
    }
    public List<CompleteDSLPckg_Region> getCompletedslpckg_regions() {
        return completedslpckg_regions;
    }

    public void addCompletedslpckg_region(Completedslpckg_region completedslpckg_region) {
        this.completedslpckg_regions.add(completedslpckg_region);
    }
    public CompleteDSLPckg_State getCompletedslpckg_state() {
        return completedslpckg_state;
    }

    public void setCompletedslpckg_state(CompleteDSLPckg_State completedslpckg_state) {
        this.completedslpckg_state = completedslpckg_state;
    }

}