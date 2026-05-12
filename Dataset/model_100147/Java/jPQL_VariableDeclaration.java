





import java.util.List;
import java.util.ArrayList;

public class jPQL_VariableDeclaration  {

    private String name;





    private jPQL_FromEntry jpql_fromentry;




    private jPQL_AliasAttributeExpression jpql_aliasattributeexpression;




    private jPQL_FromJoin jpql_fromjoin;


    public jPQL_VariableDeclaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public jPQL_FromEntry getJpql_fromentry() {
        return jpql_fromentry;
    }

    public void setJpql_fromentry(jPQL_FromEntry jpql_fromentry) {
        this.jpql_fromentry = jpql_fromentry;
    }
    public jPQL_AliasAttributeExpression getJpql_aliasattributeexpression() {
        return jpql_aliasattributeexpression;
    }

    public void setJpql_aliasattributeexpression(jPQL_AliasAttributeExpression jpql_aliasattributeexpression) {
        this.jpql_aliasattributeexpression = jpql_aliasattributeexpression;
    }
    public jPQL_FromJoin getJpql_fromjoin() {
        return jpql_fromjoin;
    }

    public void setJpql_fromjoin(jPQL_FromJoin jpql_fromjoin) {
        this.jpql_fromjoin = jpql_fromjoin;
    }

}