





import java.util.List;
import java.util.ArrayList;

public class sql_OrOrderByColumn  {






    private sql_Select sql_select;




    private List<sql_OrderByColumnFull> sql_orderbycolumnfulls;


    public sql_OrOrderByColumn(
    ) {
        this.sql_orderbycolumnfulls = new ArrayList<>();
    }

    public sql_OrOrderByColumn(
        ArrayList<sql_OrderByColumnFull> sql_orderbycolumnfulls    ) {
        this.sql_orderbycolumnfulls = sql_orderbycolumnfulls;
    }


    public sql_Select getSql_select() {
        return sql_select;
    }

    public void setSql_select(sql_Select sql_select) {
        this.sql_select = sql_select;
    }
    public List<sql_OrderByColumnFull> getSql_orderbycolumnfulls() {
        return sql_orderbycolumnfulls;
    }

    public void addSql_orderbycolumnfull(Sql_orderbycolumnfull sql_orderbycolumnfull) {
        this.sql_orderbycolumnfulls.add(sql_orderbycolumnfull);
    }

}