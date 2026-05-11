





import java.util.List;
import java.util.ArrayList;

public class sql_orderBy_OrderByAliasExpression extends OrderByExpression {

    private String alias;



    public sql_orderBy_OrderByAliasExpression(
        String alias    ) {
        super(
        );
        this.alias = alias;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }


}