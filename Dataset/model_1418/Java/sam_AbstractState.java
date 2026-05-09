





import java.util.List;
import java.util.ArrayList;

public class sam_AbstractState extends NamedItem {






    private sam_MacroState sam_macrostate;




    private sam_Automaton sam_automaton;




    private List<sam_Transition> sam_transitions;




    private sam_Automaton sam_automaton;




    private sam_MacroState sam_macrostate;




    private sam_Transition sam_transition;


    public sam_AbstractState(
    ) {
        super(
        );
        this.sam_transitions = new ArrayList<>();
    }

    public sam_AbstractState(
        ArrayList<sam_Transition> sam_transitions    ) {
        this.sam_transitions = sam_transitions;
    }


    public sam_MacroState getSam_macrostate() {
        return sam_macrostate;
    }

    public void setSam_macrostate(sam_MacroState sam_macrostate) {
        this.sam_macrostate = sam_macrostate;
    }
    public sam_Automaton getSam_automaton() {
        return sam_automaton;
    }

    public void setSam_automaton(sam_Automaton sam_automaton) {
        this.sam_automaton = sam_automaton;
    }
    public List<sam_Transition> getSam_transitions() {
        return sam_transitions;
    }

    public void addSam_transition(Sam_transition sam_transition) {
        this.sam_transitions.add(sam_transition);
    }
    public sam_Automaton getSam_automaton() {
        return sam_automaton;
    }

    public void setSam_automaton(sam_Automaton sam_automaton) {
        this.sam_automaton = sam_automaton;
    }
    public sam_MacroState getSam_macrostate() {
        return sam_macrostate;
    }

    public void setSam_macrostate(sam_MacroState sam_macrostate) {
        this.sam_macrostate = sam_macrostate;
    }
    public sam_Transition getSam_transition() {
        return sam_transition;
    }

    public void setSam_transition(sam_Transition sam_transition) {
        this.sam_transition = sam_transition;
    }

}