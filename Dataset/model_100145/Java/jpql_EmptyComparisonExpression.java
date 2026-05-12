





import java.util.List;
import java.util.ArrayList;

public class jpql_EmptyComparisonExpression extends Expression {

    private boolean isNot;





    private jpql_Variable jpql_variable;


    public jpql_EmptyComparisonExpression(
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

}