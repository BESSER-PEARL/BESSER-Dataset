





import java.util.List;
import java.util.ArrayList;

public class jPQL_LikeExpression extends Expression {

    private boolean isNot;
    private String pattern;





    private jPQL_Variable jpql_variable;


    public jPQL_LikeExpression(
        boolean isNot,        String pattern    ) {
        super(
        );
        this.isNot = isNot;
        this.pattern = pattern;
    }


    public boolean getIsnot() {
        return isNot;
    }

    public void setIsnot(boolean isNot) {
        this.isNot = isNot;
    }
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }

    public jPQL_Variable getJpql_variable() {
        return jpql_variable;
    }

    public void setJpql_variable(jPQL_Variable jpql_variable) {
        this.jpql_variable = jpql_variable;
    }

}