





import java.util.List;
import java.util.ArrayList;

public class automaton_State  {

    private String label;





    private automaton_Automaton automaton_automaton;




    private automaton_Transition automaton_transition;




    private List<automaton_Transition> automaton_transitions;




    private List<automaton_Transition> automaton_transitions;




    private automaton_Transition automaton_transition;




    private automaton_Event automaton_event;


    public automaton_State(
        String label    ) {
        this.label = label;
        this.automaton_transitions = new ArrayList<>();
        this.automaton_transitions = new ArrayList<>();
    }

    public automaton_State(
        String label        ArrayList<automaton_Transition> automaton_transitions,        ArrayList<automaton_Transition> automaton_transitions    ) {
        this.label = label;
        this.automaton_transitions = automaton_transitions;
        this.automaton_transitions = automaton_transitions;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public automaton_Automaton getAutomaton_automaton() {
        return automaton_automaton;
    }

    public void setAutomaton_automaton(automaton_Automaton automaton_automaton) {
        this.automaton_automaton = automaton_automaton;
    }
    public automaton_Transition getAutomaton_transition() {
        return automaton_transition;
    }

    public void setAutomaton_transition(automaton_Transition automaton_transition) {
        this.automaton_transition = automaton_transition;
    }
    public List<automaton_Transition> getAutomaton_transitions() {
        return automaton_transitions;
    }

    public void addAutomaton_transition(Automaton_transition automaton_transition) {
        this.automaton_transitions.add(automaton_transition);
    }
    public List<automaton_Transition> getAutomaton_transitions() {
        return automaton_transitions;
    }

    public void addAutomaton_transition(Automaton_transition automaton_transition) {
        this.automaton_transitions.add(automaton_transition);
    }
    public automaton_Transition getAutomaton_transition() {
        return automaton_transition;
    }

    public void setAutomaton_transition(automaton_Transition automaton_transition) {
        this.automaton_transition = automaton_transition;
    }
    public automaton_Event getAutomaton_event() {
        return automaton_event;
    }

    public void setAutomaton_event(automaton_Event automaton_event) {
        this.automaton_event = automaton_event;
    }

}