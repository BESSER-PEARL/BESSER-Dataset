





import java.util.List;
import java.util.ArrayList;

public class jpql_FromJoin  {

    private boolean isFetch;





    private jpql_FromClass jpql_fromclass;




    private jpql_AliasAttributeExpression jpql_aliasattributeexpression;




    private jpql_VariableDeclaration jpql_variabledeclaration;


    public jpql_FromJoin(
        boolean isFetch    ) {
        this.isFetch = isFetch;
    }


    public boolean getIsfetch() {
        return isFetch;
    }

    public void setIsfetch(boolean isFetch) {
        this.isFetch = isFetch;
    }

    public jpql_FromClass getJpql_fromclass() {
        return jpql_fromclass;
    }

    public void setJpql_fromclass(jpql_FromClass jpql_fromclass) {
        this.jpql_fromclass = jpql_fromclass;
    }
    public jpql_AliasAttributeExpression getJpql_aliasattributeexpression() {
        return jpql_aliasattributeexpression;
    }

    public void setJpql_aliasattributeexpression(jpql_AliasAttributeExpression jpql_aliasattributeexpression) {
        this.jpql_aliasattributeexpression = jpql_aliasattributeexpression;
    }
    public jpql_VariableDeclaration getJpql_variabledeclaration() {
        return jpql_variabledeclaration;
    }

    public void setJpql_variabledeclaration(jpql_VariableDeclaration jpql_variabledeclaration) {
        this.jpql_variabledeclaration = jpql_variabledeclaration;
    }

}