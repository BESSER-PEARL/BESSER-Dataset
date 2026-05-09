





import java.util.List;
import java.util.ArrayList;

public class ardurobotml_FSMEvent extends NamedElement {






    private ardurobotml_Transition ardurobotml_transition;




    private List<ardurobotml_Transition> ardurobotml_transitions;




    private ardurobotml_TimedSystem ardurobotml_timedsystem;


    public ardurobotml_FSMEvent(
    ) {
        super(
        );
        this.ardurobotml_transitions = new ArrayList<>();
    }

    public ardurobotml_FSMEvent(
        ArrayList<ardurobotml_Transition> ardurobotml_transitions    ) {
        this.ardurobotml_transitions = ardurobotml_transitions;
    }


    public ardurobotml_Transition getArdurobotml_transition() {
        return ardurobotml_transition;
    }

    public void setArdurobotml_transition(ardurobotml_Transition ardurobotml_transition) {
        this.ardurobotml_transition = ardurobotml_transition;
    }
    public List<ardurobotml_Transition> getArdurobotml_transitions() {
        return ardurobotml_transitions;
    }

    public void addArdurobotml_transition(Ardurobotml_transition ardurobotml_transition) {
        this.ardurobotml_transitions.add(ardurobotml_transition);
    }
    public ardurobotml_TimedSystem getArdurobotml_timedsystem() {
        return ardurobotml_timedsystem;
    }

    public void setArdurobotml_timedsystem(ardurobotml_TimedSystem ardurobotml_timedsystem) {
        this.ardurobotml_timedsystem = ardurobotml_timedsystem;
    }

}