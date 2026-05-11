





import java.util.List;
import java.util.ArrayList;

public class fuzzyAutomaton_Variable  {

    private String value;
    private String name;





    private fuzzyAutomaton_VariableSet fuzzyautomaton_variableset;


    public fuzzyAutomaton_Variable(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fuzzyAutomaton_VariableSet getFuzzyautomaton_variableset() {
        return fuzzyautomaton_variableset;
    }

    public void setFuzzyautomaton_variableset(fuzzyAutomaton_VariableSet fuzzyautomaton_variableset) {
        this.fuzzyautomaton_variableset = fuzzyautomaton_variableset;
    }

}