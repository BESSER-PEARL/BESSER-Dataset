





import java.util.List;
import java.util.ArrayList;

public class ram_TransitionSubstitution extends Substitution {






    private ram_Transition ram_transition;




    private List<ram_Transition> ram_transitions;


    public ram_TransitionSubstitution(
    ) {
        super(
        );
        this.ram_transitions = new ArrayList<>();
    }

    public ram_TransitionSubstitution(
        ArrayList<ram_Transition> ram_transitions    ) {
        this.ram_transitions = ram_transitions;
    }


    public ram_Transition getRam_transition() {
        return ram_transition;
    }

    public void setRam_transition(ram_Transition ram_transition) {
        this.ram_transition = ram_transition;
    }
    public List<ram_Transition> getRam_transitions() {
        return ram_transitions;
    }

    public void addRam_transition(Ram_transition ram_transition) {
        this.ram_transitions.add(ram_transition);
    }

}