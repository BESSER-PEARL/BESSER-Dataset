





import java.util.List;
import java.util.ArrayList;

public class expression_Expression  {






    private sql_column_SingleColumnExpression sql_column_singlecolumnexpression;




    private sql_from_JoinTableExpression sql_from_jointableexpression;




    private sql_groupBy_GroupByExpression sql_groupby_groupbyexpression;




    private sql_having_HavingExpression sql_having_havingexpression;




    private sql_where_WhereExpression sql_where_whereexpression;


    public expression_Expression(
    ) {
    }



    public sql_column_SingleColumnExpression getSql_column_singlecolumnexpression() {
        return sql_column_singlecolumnexpression;
    }

    public void setSql_column_singlecolumnexpression(sql_column_SingleColumnExpression sql_column_singlecolumnexpression) {
        this.sql_column_singlecolumnexpression = sql_column_singlecolumnexpression;
    }
    public sql_from_JoinTableExpression getSql_from_jointableexpression() {
        return sql_from_jointableexpression;
    }

    public void setSql_from_jointableexpression(sql_from_JoinTableExpression sql_from_jointableexpression) {
        this.sql_from_jointableexpression = sql_from_jointableexpression;
    }
    public sql_groupBy_GroupByExpression getSql_groupby_groupbyexpression() {
        return sql_groupby_groupbyexpression;
    }

    public void setSql_groupby_groupbyexpression(sql_groupBy_GroupByExpression sql_groupby_groupbyexpression) {
        this.sql_groupby_groupbyexpression = sql_groupby_groupbyexpression;
    }
    public sql_having_HavingExpression getSql_having_havingexpression() {
        return sql_having_havingexpression;
    }

    public void setSql_having_havingexpression(sql_having_HavingExpression sql_having_havingexpression) {
        this.sql_having_havingexpression = sql_having_havingexpression;
    }
    public sql_where_WhereExpression getSql_where_whereexpression() {
        return sql_where_whereexpression;
    }

    public void setSql_where_whereexpression(sql_where_WhereExpression sql_where_whereexpression) {
        this.sql_where_whereexpression = sql_where_whereexpression;
    }

}