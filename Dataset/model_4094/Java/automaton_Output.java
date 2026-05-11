





import java.util.List;
import java.util.ArrayList;

public class automaton_Output extends NamedElement {






    private automaton_Transition automaton_transition;




    private automaton_Automaton automaton_automaton;


    public automaton_Output(
    ) {
        super(
        );
    }



    public automaton_Transition getAutomaton_transition() {
        return automaton_transition;
    }

    public void setAutomaton_transition(automaton_Transition automaton_transition) {
        this.automaton_transition = automaton_transition;
    }
    public automaton_Automaton getAutomaton_automaton() {
        return automaton_automaton;
    }

    public void setAutomaton_automaton(automaton_Automaton automaton_automaton) {
        this.automaton_automaton = automaton_automaton;
    }

}