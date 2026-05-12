





import java.util.List;
import java.util.ArrayList;

public class mql_OperatorExpression extends Expression {

    private String operator;





    private mql_Variable mql_variable;


    public mql_OperatorExpression(
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

    public mql_Variable getMql_variable() {
        return mql_variable;
    }

    public void setMql_variable(mql_Variable mql_variable) {
        this.mql_variable = mql_variable;
    }

}