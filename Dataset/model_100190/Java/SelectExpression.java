





import java.util.List;
import java.util.ArrayList;

public class SelectExpression  {






    private sql_condition_ExistsCondition sql_condition_existscondition;




    private sql_set_SetExpression sql_set_setexpression;




    private sql_orderBy_OrderBySelectExpression sql_orderby_orderbyselectexpression;




    private sql_from_TableExpression sql_from_tableexpression;




    private sql_condition_InCondition sql_condition_incondition;


    public SelectExpression(
    ) {
    }



    public sql_condition_ExistsCondition getSql_condition_existscondition() {
        return sql_condition_existscondition;
    }

    public void setSql_condition_existscondition(sql_condition_ExistsCondition sql_condition_existscondition) {
        this.sql_condition_existscondition = sql_condition_existscondition;
    }
    public sql_set_SetExpression getSql_set_setexpression() {
        return sql_set_setexpression;
    }

    public void setSql_set_setexpression(sql_set_SetExpression sql_set_setexpression) {
        this.sql_set_setexpression = sql_set_setexpression;
    }
    public sql_orderBy_OrderBySelectExpression getSql_orderby_orderbyselectexpression() {
        return sql_orderby_orderbyselectexpression;
    }

    public void setSql_orderby_orderbyselectexpression(sql_orderBy_OrderBySelectExpression sql_orderby_orderbyselectexpression) {
        this.sql_orderby_orderbyselectexpression = sql_orderby_orderbyselectexpression;
    }
    public sql_from_TableExpression getSql_from_tableexpression() {
        return sql_from_tableexpression;
    }

    public void setSql_from_tableexpression(sql_from_TableExpression sql_from_tableexpression) {
        this.sql_from_tableexpression = sql_from_tableexpression;
    }
    public sql_condition_InCondition getSql_condition_incondition() {
        return sql_condition_incondition;
    }

    public void setSql_condition_incondition(sql_condition_InCondition sql_condition_incondition) {
        this.sql_condition_incondition = sql_condition_incondition;
    }

}