





import java.util.List;
import java.util.ArrayList;

public class mql_InExpression extends Expression {

    private boolean isNot;





    private mql_Variable mql_variable;


    public mql_InExpression(
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

    public mql_Variable getMql_variable() {
        return mql_variable;
    }

    public void setMql_variable(mql_Variable mql_variable) {
        this.mql_variable = mql_variable;
    }

}