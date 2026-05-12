





import java.util.List;
import java.util.ArrayList;

public class jPQL_FromJoin  {

    private boolean isFetch;





    private jPQL_AliasAttributeExpression jpql_aliasattributeexpression;


    public jPQL_FromJoin(
        boolean isFetch    ) {
        this.isFetch = isFetch;
    }


    public boolean getIsfetch() {
        return isFetch;
    }

    public void setIsfetch(boolean isFetch) {
        this.isFetch = isFetch;
    }

    public jPQL_AliasAttributeExpression getJpql_aliasattributeexpression() {
        return jpql_aliasattributeexpression;
    }

    public void setJpql_aliasattributeexpression(jPQL_AliasAttributeExpression jpql_aliasattributeexpression) {
        this.jpql_aliasattributeexpression = jpql_aliasattributeexpression;
    }

}