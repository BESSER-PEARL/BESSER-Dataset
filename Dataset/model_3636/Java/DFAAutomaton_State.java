





import java.util.List;
import java.util.ArrayList;

public class DFAAutomaton_State  {

    private String name;
    private boolean isInitial;
    private boolean isFinal;





    private DFAAutomaton_Automaton dfaautomaton_automaton;


    public DFAAutomaton_State(
        String name,        boolean isInitial,        boolean isFinal    ) {
        this.name = name;
        this.isInitial = isInitial;
        this.isFinal = isFinal;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsinitial() {
        return isInitial;
    }

    public void setIsinitial(boolean isInitial) {
        this.isInitial = isInitial;
    }
    public boolean getIsfinal() {
        return isFinal;
    }

    public void setIsfinal(boolean isFinal) {
        this.isFinal = isFinal;
    }

    public DFAAutomaton_Automaton getDfaautomaton_automaton() {
        return dfaautomaton_automaton;
    }

    public void setDfaautomaton_automaton(DFAAutomaton_Automaton dfaautomaton_automaton) {
        this.dfaautomaton_automaton = dfaautomaton_automaton;
    }

}