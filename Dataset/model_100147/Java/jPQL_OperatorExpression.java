





import java.util.List;
import java.util.ArrayList;

public class jPQL_OperatorExpression extends Expression {

    private String operator;





    private jPQL_Variable jpql_variable;


    public jPQL_OperatorExpression(
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

    public jPQL_Variable getJpql_variable() {
        return jpql_variable;
    }

    public void setJpql_variable(jPQL_Variable jpql_variable) {
        this.jpql_variable = jpql_variable;
    }

}