





import java.util.List;
import java.util.ArrayList;

public class sql_OrGroupByColumn  {






    private List<sql_GroupByColumnFull> sql_groupbycolumnfulls;




    private sql_Select sql_select;


    public sql_OrGroupByColumn(
    ) {
        this.sql_groupbycolumnfulls = new ArrayList<>();
    }

    public sql_OrGroupByColumn(
        ArrayList<sql_GroupByColumnFull> sql_groupbycolumnfulls    ) {
        this.sql_groupbycolumnfulls = sql_groupbycolumnfulls;
    }


    public List<sql_GroupByColumnFull> getSql_groupbycolumnfulls() {
        return sql_groupbycolumnfulls;
    }

    public void addSql_groupbycolumnfull(Sql_groupbycolumnfull sql_groupbycolumnfull) {
        this.sql_groupbycolumnfulls.add(sql_groupbycolumnfull);
    }
    public sql_Select getSql_select() {
        return sql_select;
    }

    public void setSql_select(sql_Select sql_select) {
        this.sql_select = sql_select;
    }

}