





import java.util.List;
import java.util.ArrayList;

public class jPQL_FromJoin  {

    private boolean isFetch;





    private jPQL_AliasAttributeExpression jpql_aliasattributeexpression;




    private jPQL_VariableDeclaration jpql_variabledeclaration;




    private jPQL_FromClass jpql_fromclass;


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
    public jPQL_VariableDeclaration getJpql_variabledeclaration() {
        return jpql_variabledeclaration;
    }

    public void setJpql_variabledeclaration(jPQL_VariableDeclaration jpql_variabledeclaration) {
        this.jpql_variabledeclaration = jpql_variabledeclaration;
    }
    public jPQL_FromClass getJpql_fromclass() {
        return jpql_fromclass;
    }

    public void setJpql_fromclass(jPQL_FromClass jpql_fromclass) {
        this.jpql_fromclass = jpql_fromclass;
    }

}