





import java.util.List;
import java.util.ArrayList;

public class jpql_OperatorExpression extends Expression {

    private String operator;





    private jpql_Variable jpql_variable;


    public jpql_OperatorExpression(
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

    public jpql_Variable getJpql_variable() {
        return jpql_variable;
    }

    public void setJpql_variable(jpql_Variable jpql_variable) {
        this.jpql_variable = jpql_variable;
    }

}