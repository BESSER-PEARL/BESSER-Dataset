





import java.util.List;
import java.util.ArrayList;

public class timedAutomata_expressions_AssignmentExpression extends Expression {

    private String operator;



    public timedAutomata_expressions_AssignmentExpression(
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


}