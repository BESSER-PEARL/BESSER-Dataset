





import java.util.List;
import java.util.ArrayList;

public class mql_BetweenExpression extends Expression {

    private boolean isNot;





    private mql_Value mql_value;




    private mql_Value mql_value;




    private mql_Variable mql_variable;


    public mql_BetweenExpression(
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

    public mql_Value getMql_value() {
        return mql_value;
    }

    public void setMql_value(mql_Value mql_value) {
        this.mql_value = mql_value;
    }
    public mql_Value getMql_value() {
        return mql_value;
    }

    public void setMql_value(mql_Value mql_value) {
        this.mql_value = mql_value;
    }
    public mql_Variable getMql_variable() {
        return mql_variable;
    }

    public void setMql_variable(mql_Variable mql_variable) {
        this.mql_variable = mql_variable;
    }

}