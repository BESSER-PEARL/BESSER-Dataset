





import java.util.List;
import java.util.ArrayList;

public class mql_SelectAggregateExpression extends SelectExpression {

    private boolean isDistinct;





    private mql_AliasAttributeExpression mql_aliasattributeexpression;


    public mql_SelectAggregateExpression(
        boolean isDistinct    ) {
        super(
        );
        this.isDistinct = isDistinct;
    }


    public boolean getIsdistinct() {
        return isDistinct;
    }

    public void setIsdistinct(boolean isDistinct) {
        this.isDistinct = isDistinct;
    }

    public mql_AliasAttributeExpression getMql_aliasattributeexpression() {
        return mql_aliasattributeexpression;
    }

    public void setMql_aliasattributeexpression(mql_AliasAttributeExpression mql_aliasattributeexpression) {
        this.mql_aliasattributeexpression = mql_aliasattributeexpression;
    }

}