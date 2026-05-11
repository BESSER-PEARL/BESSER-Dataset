





import java.util.List;
import java.util.ArrayList;

public class sql_ColumnFull extends PivotForClause {






    private sql_OrderByColumnFull sql_orderbycolumnfull;




    private sql_GroupByColumnFull sql_groupbycolumnfull;




    private sql_ColumnOperand sql_columnoperand;


    public sql_ColumnFull(
    ) {
        super(
        );
    }



    public sql_OrderByColumnFull getSql_orderbycolumnfull() {
        return sql_orderbycolumnfull;
    }

    public void setSql_orderbycolumnfull(sql_OrderByColumnFull sql_orderbycolumnfull) {
        this.sql_orderbycolumnfull = sql_orderbycolumnfull;
    }
    public sql_GroupByColumnFull getSql_groupbycolumnfull() {
        return sql_groupbycolumnfull;
    }

    public void setSql_groupbycolumnfull(sql_GroupByColumnFull sql_groupbycolumnfull) {
        this.sql_groupbycolumnfull = sql_groupbycolumnfull;
    }
    public sql_ColumnOperand getSql_columnoperand() {
        return sql_columnoperand;
    }

    public void setSql_columnoperand(sql_ColumnOperand sql_columnoperand) {
        this.sql_columnoperand = sql_columnoperand;
    }

}