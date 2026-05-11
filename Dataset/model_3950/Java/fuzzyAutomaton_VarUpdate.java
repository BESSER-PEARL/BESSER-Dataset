





import java.util.List;
import java.util.ArrayList;

public class fuzzyAutomaton_VarUpdate  {

    private String expression;





    private fuzzyAutomaton_Variable fuzzyautomaton_variable;




    private fuzzyAutomaton_VarTransformation fuzzyautomaton_vartransformation;


    public fuzzyAutomaton_VarUpdate(
        String expression    ) {
        this.expression = expression;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public fuzzyAutomaton_Variable getFuzzyautomaton_variable() {
        return fuzzyautomaton_variable;
    }

    public void setFuzzyautomaton_variable(fuzzyAutomaton_Variable fuzzyautomaton_variable) {
        this.fuzzyautomaton_variable = fuzzyautomaton_variable;
    }
    public fuzzyAutomaton_VarTransformation getFuzzyautomaton_vartransformation() {
        return fuzzyautomaton_vartransformation;
    }

    public void setFuzzyautomaton_vartransformation(fuzzyAutomaton_VarTransformation fuzzyautomaton_vartransformation) {
        this.fuzzyautomaton_vartransformation = fuzzyautomaton_vartransformation;
    }

}