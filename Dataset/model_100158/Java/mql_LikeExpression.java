





import java.util.List;
import java.util.ArrayList;

public class mql_LikeExpression extends Expression {

    private String pattern;
    private boolean isNot;





    private mql_Variable mql_variable;


    public mql_LikeExpression(
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

    public mql_Variable getMql_variable() {
        return mql_variable;
    }

    public void setMql_variable(mql_Variable mql_variable) {
        this.mql_variable = mql_variable;
    }

}