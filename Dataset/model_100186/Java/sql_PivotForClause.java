





import java.util.List;
import java.util.ArrayList;

public class sql_PivotForClause  {






    private sql_PivotTable sql_pivottable;




    private sql_UnpivotTable sql_unpivottable;


    public sql_PivotForClause(
    ) {
    }



    public sql_PivotTable getSql_pivottable() {
        return sql_pivottable;
    }

    public void setSql_pivottable(sql_PivotTable sql_pivottable) {
        this.sql_pivottable = sql_pivottable;
    }
    public sql_UnpivotTable getSql_unpivottable() {
        return sql_unpivottable;
    }

    public void setSql_unpivottable(sql_UnpivotTable sql_unpivottable) {
        this.sql_unpivottable = sql_unpivottable;
    }

}