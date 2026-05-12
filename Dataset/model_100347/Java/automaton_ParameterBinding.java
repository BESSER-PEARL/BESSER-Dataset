





import java.util.List;
import java.util.ArrayList;

public class automaton_ParameterBinding  {

    private String value;
    private String symbolicName;





    private automaton_ParameterTable automaton_parametertable;




    private automaton_ParameterTable automaton_parametertable;


    public automaton_ParameterBinding(
        String value,        String symbolicName    ) {
        this.value = value;
        this.symbolicName = symbolicName;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getSymbolicname() {
        return symbolicName;
    }

    public void setSymbolicname(String symbolicName) {
        this.symbolicName = symbolicName;
    }

    public automaton_ParameterTable getAutomaton_parametertable() {
        return automaton_parametertable;
    }

    public void setAutomaton_parametertable(automaton_ParameterTable automaton_parametertable) {
        this.automaton_parametertable = automaton_parametertable;
    }
    public automaton_ParameterTable getAutomaton_parametertable() {
        return automaton_parametertable;
    }

    public void setAutomaton_parametertable(automaton_ParameterTable automaton_parametertable) {
        this.automaton_parametertable = automaton_parametertable;
    }

}