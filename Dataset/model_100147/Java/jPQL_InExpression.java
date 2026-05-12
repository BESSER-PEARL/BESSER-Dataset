





import java.util.List;
import java.util.ArrayList;

public class jPQL_InExpression extends Expression {

    private boolean isNot;





    private jPQL_Variable jpql_variable;


    public jPQL_InExpression(
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

}