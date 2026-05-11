





import java.util.List;
import java.util.ArrayList;

public class sql_UsingCols  {






    private sql_JoinCondition sql_joincondition;




    private List<sql_DbObjectName> sql_dbobjectnames;


    public sql_UsingCols(
    ) {
        this.sql_dbobjectnames = new ArrayList<>();
    }

    public sql_UsingCols(
        ArrayList<sql_DbObjectName> sql_dbobjectnames    ) {
        this.sql_dbobjectnames = sql_dbobjectnames;
    }


    public sql_JoinCondition getSql_joincondition() {
        return sql_joincondition;
    }

    public void setSql_joincondition(sql_JoinCondition sql_joincondition) {
        this.sql_joincondition = sql_joincondition;
    }
    public List<sql_DbObjectName> getSql_dbobjectnames() {
        return sql_dbobjectnames;
    }

    public void addSql_dbobjectname(Sql_dbobjectname sql_dbobjectname) {
        this.sql_dbobjectnames.add(sql_dbobjectname);
    }

}