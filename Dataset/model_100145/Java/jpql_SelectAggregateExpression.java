





import java.util.List;
import java.util.ArrayList;

public class jpql_SelectAggregateExpression extends SelectExpression {

    private boolean isDistinct;





    private jpql_AliasAttributeExpression jpql_aliasattributeexpression;


    public jpql_SelectAggregateExpression(
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

    public jpql_AliasAttributeExpression getJpql_aliasattributeexpression() {
        return jpql_aliasattributeexpression;
    }

    public void setJpql_aliasattributeexpression(jpql_AliasAttributeExpression jpql_aliasattributeexpression) {
        this.jpql_aliasattributeexpression = jpql_aliasattributeexpression;
    }

}