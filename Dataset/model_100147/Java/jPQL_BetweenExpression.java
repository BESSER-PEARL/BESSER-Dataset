





import java.util.List;
import java.util.ArrayList;

public class jPQL_BetweenExpression extends Expression {

    private boolean isNot;





    private jPQL_Variable jpql_variable;




    private jPQL_Value jpql_value;




    private jPQL_Value jpql_value;


    public jPQL_BetweenExpression(
        boolean isNot    ) {
        super(
        );
        this.isNot = isNot;
    }


    public boolean getIsnot() {
        return isNot;
    }

    public void setIsnot(boolean isNot) {
        this.isNot = isNot;
    }

    public jPQL_Variable getJpql_variable() {
        return jpql_variable;
    }

    public void setJpql_variable(jPQL_Variable jpql_variable) {
        this.jpql_variable = jpql_variable;
    }
    public jPQL_Value getJpql_value() {
        return jpql_value;
    }

    public void setJpql_value(jPQL_Value jpql_value) {
        this.jpql_value = jpql_value;
    }
    public jPQL_Value getJpql_value() {
        return jpql_value;
    }

    public void setJpql_value(jPQL_Value jpql_value) {
        this.jpql_value = jpql_value;
    }

}