





import java.util.List;
import java.util.ArrayList;

public class mql_SelectConstructorExpression extends SelectExpression {

    private String name;





    private List<mql_AliasAttributeExpression> mql_aliasattributeexpressions;


    public mql_SelectConstructorExpression(
        String name    ) {
        super(
        );
        this.name = name;
        this.mql_aliasattributeexpressions = new ArrayList<>();
    }

    public mql_SelectConstructorExpression(
        String name        ArrayList<mql_AliasAttributeExpression> mql_aliasattributeexpressions    ) {
        this.name = name;
        this.mql_aliasattributeexpressions = mql_aliasattributeexpressions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<mql_AliasAttributeExpression> getMql_aliasattributeexpressions() {
        return mql_aliasattributeexpressions;
    }

    public void addMql_aliasattributeexpression(Mql_aliasattributeexpression mql_aliasattributeexpression) {
        this.mql_aliasattributeexpressions.add(mql_aliasattributeexpression);
    }

}