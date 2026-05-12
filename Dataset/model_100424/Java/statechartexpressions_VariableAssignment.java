





import java.util.List;
import java.util.ArrayList;

public class statechartexpressions_VariableAssignment extends Statement {

    private String operator;





    private statechartexpressions_VariableReference statechartexpressions_variablereference;


    public statechartexpressions_VariableAssignment(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public statechartexpressions_VariableReference getStatechartexpressions_variablereference() {
        return statechartexpressions_variablereference;
    }

    public void setStatechartexpressions_variablereference(statechartexpressions_VariableReference statechartexpressions_variablereference) {
        this.statechartexpressions_variablereference = statechartexpressions_variablereference;
    }

}