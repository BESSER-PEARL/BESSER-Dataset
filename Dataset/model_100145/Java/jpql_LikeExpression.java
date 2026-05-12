





import java.util.List;
import java.util.ArrayList;

public class jpql_LikeExpression extends Expression {

    private String pattern;
    private boolean isNot;





    private jpql_Variable jpql_variable;


    public jpql_LikeExpression(
        String pattern,        boolean isNot    ) {
        super(
        );
        this.pattern = pattern;
        this.isNot = isNot;
    }


    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
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