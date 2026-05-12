





import java.util.List;
import java.util.ArrayList;

public class jpql_BetweenExpression extends Expression {

    private boolean isNot;





    private jpql_Variable jpql_variable;




    private jpql_Value jpql_value;




    private jpql_Value jpql_value;


    public jpql_BetweenExpression(
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

    public jpql_Variable getJpql_variable() {
        return jpql_variable;
    }

    public void setJpql_variable(jpql_Variable jpql_variable) {
        this.jpql_variable = jpql_variable;
    }
    public jpql_Value getJpql_value() {
        return jpql_value;
    }

    public void setJpql_value(jpql_Value jpql_value) {
        this.jpql_value = jpql_value;
    }
    public jpql_Value getJpql_value() {
        return jpql_value;
    }

    public void setJpql_value(jpql_Value jpql_value) {
        this.jpql_value = jpql_value;
    }

}