





import java.util.List;
import java.util.ArrayList;

public class mql_CollectionExpression extends Expression {

    private boolean isNot;





    private mql_AliasAttributeExpression mql_aliasattributeexpression;




    private mql_Variable mql_variable;


    public mql_CollectionExpression(
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

    public mql_AliasAttributeExpression getMql_aliasattributeexpression() {
        return mql_aliasattributeexpression;
    }

    public void setMql_aliasattributeexpression(mql_AliasAttributeExpression mql_aliasattributeexpression) {
        this.mql_aliasattributeexpression = mql_aliasattributeexpression;
    }
    public mql_Variable getMql_variable() {
        return mql_variable;
    }

    public void setMql_variable(mql_Variable mql_variable) {
        this.mql_variable = mql_variable;
    }

}