





import java.util.List;
import java.util.ArrayList;

public class jPQL_CollectionExpression extends Expression {

    private boolean isNot;





    private jPQL_Variable jpql_variable;




    private jPQL_AliasAttributeExpression jpql_aliasattributeexpression;


    public jPQL_CollectionExpression(
        boolean isNot    ) {
        super(
        );
        this.isNot = isNot;
    }


    public boolean getIsnot() {
        return isNot;
    }

    public void setIsnot(boolean isNot) {
        this.isNot = isNot;
    }

    public jPQL_Variable getJpql_variable() {
        return jpql_variable;
    }

    public void setJpql_variable(jPQL_Variable jpql_variable) {
        this.jpql_variable = jpql_variable;
    }
    public jPQL_AliasAttributeExpression getJpql_aliasattributeexpression() {
        return jpql_aliasattributeexpression;
    }

    public void setJpql_aliasattributeexpression(jPQL_AliasAttributeExpression jpql_aliasattributeexpression) {
        this.jpql_aliasattributeexpression = jpql_aliasattributeexpression;
    }

}