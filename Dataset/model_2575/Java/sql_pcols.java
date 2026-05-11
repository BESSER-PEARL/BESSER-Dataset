





import java.util.List;
import java.util.ArrayList;

public class sql_pcols extends PivotCol {






    private List<sql_DbObjectName> sql_dbobjectnames;


    public sql_pcols(
    ) {
        super(
        );
        this.sql_dbobjectnames = new ArrayList<>();
    }

    public sql_pcols(
        ArrayList<sql_DbObjectName> sql_dbobjectnames    ) {
        this.sql_dbobjectnames = sql_dbobjectnames;
    }


    public List<sql_DbObjectName> getSql_dbobjectnames() {
        return sql_dbobjectnames;
    }

    public void addSql_dbobjectname(Sql_dbobjectname sql_dbobjectname) {
        this.sql_dbobjectnames.add(sql_dbobjectname);
    }

}