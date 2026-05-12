





import java.util.List;
import java.util.ArrayList;

public class jPQL_SelectAggregateExpression extends SelectExpression {

    private boolean isDistinct;





    private jPQL_AliasAttributeExpression jpql_aliasattributeexpression;


    public jPQL_SelectAggregateExpression(
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

    public jPQL_AliasAttributeExpression getJpql_aliasattributeexpression() {
        return jpql_aliasattributeexpression;
    }

    public void setJpql_aliasattributeexpression(jPQL_AliasAttributeExpression jpql_aliasattributeexpression) {
        this.jpql_aliasattributeexpression = jpql_aliasattributeexpression;
    }

}