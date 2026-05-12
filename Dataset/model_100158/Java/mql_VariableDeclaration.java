





import java.util.List;
import java.util.ArrayList;

public class mql_VariableDeclaration  {

    private String name;





    private mql_AliasAttributeExpression mql_aliasattributeexpression;




    private mql_FromEntry mql_fromentry;


    public mql_VariableDeclaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mql_AliasAttributeExpression getMql_aliasattributeexpression() {
        return mql_aliasattributeexpression;
    }

    public void setMql_aliasattributeexpression(mql_AliasAttributeExpression mql_aliasattributeexpression) {
        this.mql_aliasattributeexpression = mql_aliasattributeexpression;
    }
    public mql_FromEntry getMql_fromentry() {
        return mql_fromentry;
    }

    public void setMql_fromentry(mql_FromEntry mql_fromentry) {
        this.mql_fromentry = mql_fromentry;
    }

}