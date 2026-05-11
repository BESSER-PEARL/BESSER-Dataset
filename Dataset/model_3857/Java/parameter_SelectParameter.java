





import java.util.List;
import java.util.ArrayList;

public class parameter_SelectParameter  {






    private sql_select_SelectExpression sql_select_selectexpression;




    private sql_column_SingleColumnExpression sql_column_singlecolumnexpression;


    public parameter_SelectParameter(
    ) {
    }



    public sql_select_SelectExpression getSql_select_selectexpression() {
        return sql_select_selectexpression;
    }

    public void setSql_select_selectexpression(sql_select_SelectExpression sql_select_selectexpression) {
        this.sql_select_selectexpression = sql_select_selectexpression;
    }
    public sql_column_SingleColumnExpression getSql_column_singlecolumnexpression() {
        return sql_column_singlecolumnexpression;
    }

    public void setSql_column_singlecolumnexpression(sql_column_SingleColumnExpression sql_column_singlecolumnexpression) {
        this.sql_column_singlecolumnexpression = sql_column_singlecolumnexpression;
    }

}