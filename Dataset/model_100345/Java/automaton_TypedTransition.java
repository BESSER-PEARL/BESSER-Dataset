





import java.util.List;
import java.util.ArrayList;

public class automaton_TypedTransition extends Transition {






    private List<automaton_Guard> automaton_guards;




    private automaton_Guard automaton_guard;




    private List<automaton_Parameter> automaton_parameters;




    private automaton_Parameter automaton_parameter;


    public automaton_TypedTransition(
    ) {
        super(
        );
        this.automaton_guards = new ArrayList<>();
        this.automaton_parameters = new ArrayList<>();
    }

    public automaton_TypedTransition(
        ArrayList<automaton_Guard> automaton_guards,        ArrayList<automaton_Parameter> automaton_parameters    ) {
        this.automaton_guards = automaton_guards;
        this.automaton_parameters = automaton_parameters;
    }


    public List<automaton_Guard> getAutomaton_guards() {
        return automaton_guards;
    }

    public void addAutomaton_guard(Automaton_guard automaton_guard) {
        this.automaton_guards.add(automaton_guard);
    }
    public automaton_Guard getAutomaton_guard() {
        return automaton_guard;
    }

    public void setAutomaton_guard(automaton_Guard automaton_guard) {
        this.automaton_guard = automaton_guard;
    }
    public List<automaton_Parameter> getAutomaton_parameters() {
        return automaton_parameters;
    }

    public void addAutomaton_parameter(Automaton_parameter automaton_parameter) {
        this.automaton_parameters.add(automaton_parameter);
    }
    public automaton_Parameter getAutomaton_parameter() {
        return automaton_parameter;
    }

    public void setAutomaton_parameter(automaton_Parameter automaton_parameter) {
        this.automaton_parameter = automaton_parameter;
    }

}