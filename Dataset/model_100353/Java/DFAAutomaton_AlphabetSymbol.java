





import java.util.List;
import java.util.ArrayList;

public class DFAAutomaton_AlphabetSymbol  {

    private String symbol;





    private DFAAutomaton_Transition dfaautomaton_transition;




    private DFAAutomaton_Automaton dfaautomaton_automaton;


    public DFAAutomaton_AlphabetSymbol(
        String symbol    ) {
        this.symbol = symbol;
    }


    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public DFAAutomaton_Transition getDfaautomaton_transition() {
        return dfaautomaton_transition;
    }

    public void setDfaautomaton_transition(DFAAutomaton_Transition dfaautomaton_transition) {
        this.dfaautomaton_transition = dfaautomaton_transition;
    }
    public DFAAutomaton_Automaton getDfaautomaton_automaton() {
        return dfaautomaton_automaton;
    }

    public void setDfaautomaton_automaton(DFAAutomaton_Automaton dfaautomaton_automaton) {
        this.dfaautomaton_automaton = dfaautomaton_automaton;
    }

}