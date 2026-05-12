





import java.util.List;
import java.util.ArrayList;

public class mql_FromJoin  {

    private boolean isFetch;





    private mql_FromClass mql_fromclass;




    private mql_VariableDeclaration mql_variabledeclaration;




    private mql_AliasAttributeExpression mql_aliasattributeexpression;


    public mql_FromJoin(
        boolean isFetch    ) {
        this.isFetch = isFetch;
    }


    public boolean getIsfetch() {
        return isFetch;
    }

    public void setIsfetch(boolean isFetch) {
        this.isFetch = isFetch;
    }

    public mql_FromClass getMql_fromclass() {
        return mql_fromclass;
    }

    public void setMql_fromclass(mql_FromClass mql_fromclass) {
        this.mql_fromclass = mql_fromclass;
    }
    public mql_VariableDeclaration getMql_variabledeclaration() {
        return mql_variabledeclaration;
    }

    public void setMql_variabledeclaration(mql_VariableDeclaration mql_variabledeclaration) {
        this.mql_variabledeclaration = mql_variabledeclaration;
    }
    public mql_AliasAttributeExpression getMql_aliasattributeexpression() {
        return mql_aliasattributeexpression;
    }

    public void setMql_aliasattributeexpression(mql_AliasAttributeExpression mql_aliasattributeexpression) {
        this.mql_aliasattributeexpression = mql_aliasattributeexpression;
    }

}