





import java.util.List;
import java.util.ArrayList;

public class automaton_Parameter  {

    private String symbolicName;
    private int position;





    private automaton_TypedTransition automaton_typedtransition;




    private automaton_TypedTransition automaton_typedtransition;


    public automaton_Parameter(
        String symbolicName,        int position    ) {
        this.symbolicName = symbolicName;
        this.position = position;
    }


    public String getSymbolicname() {
        return symbolicName;
    }

    public void setSymbolicname(String symbolicName) {
        this.symbolicName = symbolicName;
    }
    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }

    public automaton_TypedTransition getAutomaton_typedtransition() {
        return automaton_typedtransition;
    }

    public void setAutomaton_typedtransition(automaton_TypedTransition automaton_typedtransition) {
        this.automaton_typedtransition = automaton_typedtransition;
    }
    public automaton_TypedTransition getAutomaton_typedtransition() {
        return automaton_typedtransition;
    }

    public void setAutomaton_typedtransition(automaton_TypedTransition automaton_typedtransition) {
        this.automaton_typedtransition = automaton_typedtransition;
    }

}