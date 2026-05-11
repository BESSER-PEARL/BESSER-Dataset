





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Region extends NamedElement {






    private List<CompleteDSLPckg_Transition> completedslpckg_transitions;




    private CompleteDSLPckg_StateMachine completedslpckg_statemachine;




    private CompleteDSLPckg_StateMachine completedslpckg_statemachine;


    public CompleteDSLPckg_Region(
    ) {
        super(
        );
        this.completedslpckg_transitions = new ArrayList<>();
    }

    public CompleteDSLPckg_Region(
        ArrayList<CompleteDSLPckg_Transition> completedslpckg_transitions    ) {
        this.completedslpckg_transitions = completedslpckg_transitions;
    }


    public List<CompleteDSLPckg_Transition> getCompletedslpckg_transitions() {
        return completedslpckg_transitions;
    }

    public void addCompletedslpckg_transition(Completedslpckg_transition completedslpckg_transition) {
        this.completedslpckg_transitions.add(completedslpckg_transition);
    }
    public CompleteDSLPckg_StateMachine getCompletedslpckg_statemachine() {
        return completedslpckg_statemachine;
    }

    public void setCompletedslpckg_statemachine(CompleteDSLPckg_StateMachine completedslpckg_statemachine) {
        this.completedslpckg_statemachine = completedslpckg_statemachine;
    }
    public CompleteDSLPckg_StateMachine getCompletedslpckg_statemachine() {
        return completedslpckg_statemachine;
    }

    public void setCompletedslpckg_statemachine(CompleteDSLPckg_StateMachine completedslpckg_statemachine) {
        this.completedslpckg_statemachine = completedslpckg_statemachine;
    }

}