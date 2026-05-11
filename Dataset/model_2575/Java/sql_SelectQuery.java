





import java.util.List;
import java.util.ArrayList;

public class sql_SelectQuery  {






    private sql_SubQueryOperand sql_subqueryoperand;




    private sql_WithQuery sql_withquery;


    public sql_SelectQuery(
    ) {
    }



    public sql_SubQueryOperand getSql_subqueryoperand() {
        return sql_subqueryoperand;
    }

    public void setSql_subqueryoperand(sql_SubQueryOperand sql_subqueryoperand) {
        this.sql_subqueryoperand = sql_subqueryoperand;
    }
    public sql_WithQuery getSql_withquery() {
        return sql_withquery;
    }

    public void setSql_withquery(sql_WithQuery sql_withquery) {
        this.sql_withquery = sql_withquery;
    }

}