





import java.util.List;
import java.util.ArrayList;

public class sam_State extends AbstractState {






    private List<sam_Transition> sam_transitions;




    private sam_Transition sam_transition;


    public sam_State(
    ) {
        super(
        );
        this.sam_transitions = new ArrayList<>();
    }

    public sam_State(
        ArrayList<sam_Transition> sam_transitions    ) {
        this.sam_transitions = sam_transitions;
    }


    public List<sam_Transition> getSam_transitions() {
        return sam_transitions;
    }

    public void addSam_transition(Sam_transition sam_transition) {
        this.sam_transitions.add(sam_transition);
    }
    public sam_Transition getSam_transition() {
        return sam_transition;
    }

    public void setSam_transition(sam_Transition sam_transition) {
        this.sam_transition = sam_transition;
    }

}