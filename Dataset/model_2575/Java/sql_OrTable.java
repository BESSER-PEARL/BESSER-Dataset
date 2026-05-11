





import java.util.List;
import java.util.ArrayList;

public class sql_OrTable  {






    private List<sql_FromTable> sql_fromtables;




    private sql_Select sql_select;


    public sql_OrTable(
    ) {
        this.sql_fromtables = new ArrayList<>();
    }

    public sql_OrTable(
        ArrayList<sql_FromTable> sql_fromtables    ) {
        this.sql_fromtables = sql_fromtables;
    }


    public List<sql_FromTable> getSql_fromtables() {
        return sql_fromtables;
    }

    public void addSql_fromtable(Sql_fromtable sql_fromtable) {
        this.sql_fromtables.add(sql_fromtable);
    }
    public sql_Select getSql_select() {
        return sql_select;
    }

    public void setSql_select(sql_Select sql_select) {
        this.sql_select = sql_select;
    }

}