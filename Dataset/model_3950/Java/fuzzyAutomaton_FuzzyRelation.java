





import java.util.List;
import java.util.ArrayList;

public class fuzzyAutomaton_FuzzyRelation  {

    private String expression2;
    private String expression3;
    private String delta;
    private String tFRelation;
    private String expression1;





    private fuzzyAutomaton_FuzzyConstraint fuzzyautomaton_fuzzyconstraint;


    public fuzzyAutomaton_FuzzyRelation(
        String expression2,        String expression3,        String delta,        String tFRelation,        String expression1    ) {
        this.expression2 = expression2;
        this.expression3 = expression3;
        this.delta = delta;
        this.tFRelation = tFRelation;
        this.expression1 = expression1;
    }


    public String getExpression2() {
        return expression2;
    }

    public void setExpression2(String expression2) {
        this.expression2 = expression2;
    }
    public String getExpression3() {
        return expression3;
    }

    public void setExpression3(String expression3) {
        this.expression3 = expression3;
    }
    public String getDelta() {
        return delta;
    }

    public void setDelta(String delta) {
        this.delta = delta;
    }
    public String getTfrelation() {
        return tFRelation;
    }

    public void setTfrelation(String tFRelation) {
        this.tFRelation = tFRelation;
    }
    public String getExpression1() {
        return expression1;
    }

    public void setExpression1(String expression1) {
        this.expression1 = expression1;
    }

    public fuzzyAutomaton_FuzzyConstraint getFuzzyautomaton_fuzzyconstraint() {
        return fuzzyautomaton_fuzzyconstraint;
    }

    public void setFuzzyautomaton_fuzzyconstraint(fuzzyAutomaton_FuzzyConstraint fuzzyautomaton_fuzzyconstraint) {
        this.fuzzyautomaton_fuzzyconstraint = fuzzyautomaton_fuzzyconstraint;
    }

}