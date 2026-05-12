





import java.util.List;
import java.util.ArrayList;

public class jpql_SelectConstructorExpression extends SelectExpression {

    private String name;





    private List<jpql_AliasAttributeExpression> jpql_aliasattributeexpressions;


    public jpql_SelectConstructorExpression(
        String name    ) {
        super(
        );
        this.name = name;
        this.jpql_aliasattributeexpressions = new ArrayList<>();
    }

    public jpql_SelectConstructorExpression(
        String name        ArrayList<jpql_AliasAttributeExpression> jpql_aliasattributeexpressions    ) {
        this.name = name;
        this.jpql_aliasattributeexpressions = jpql_aliasattributeexpressions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<jpql_AliasAttributeExpression> getJpql_aliasattributeexpressions() {
        return jpql_aliasattributeexpressions;
    }

    public void addJpql_aliasattributeexpression(Jpql_aliasattributeexpression jpql_aliasattributeexpression) {
        this.jpql_aliasattributeexpressions.add(jpql_aliasattributeexpression);
    }

}