





import java.util.List;
import java.util.ArrayList;

public class jpql_VariableDeclaration  {

    private String name;





    private jpql_AliasAttributeExpression jpql_aliasattributeexpression;




    private jpql_FromEntry jpql_fromentry;


    public jpql_VariableDeclaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public jpql_AliasAttributeExpression getJpql_aliasattributeexpression() {
        return jpql_aliasattributeexpression;
    }

    public void setJpql_aliasattributeexpression(jpql_AliasAttributeExpression jpql_aliasattributeexpression) {
        this.jpql_aliasattributeexpression = jpql_aliasattributeexpression;
    }
    public jpql_FromEntry getJpql_fromentry() {
        return jpql_fromentry;
    }

    public void setJpql_fromentry(jpql_FromEntry jpql_fromentry) {
        this.jpql_fromentry = jpql_fromentry;
    }

}