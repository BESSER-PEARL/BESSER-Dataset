





import java.util.List;
import java.util.ArrayList;

public class sql_TableOrAlias  {

    private String alias;





    private sql_FromTable sql_fromtable;




    private sql_DbObjectName sql_dbobjectname;


    public sql_TableOrAlias(
        String alias    ) {
        this.alias = alias;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }

    public sql_FromTable getSql_fromtable() {
        return sql_fromtable;
    }

    public void setSql_fromtable(sql_FromTable sql_fromtable) {
        this.sql_fromtable = sql_fromtable;
    }
    public sql_DbObjectName getSql_dbobjectname() {
        return sql_dbobjectname;
    }

    public void setSql_dbobjectname(sql_DbObjectName sql_dbobjectname) {
        this.sql_dbobjectname = sql_dbobjectname;
    }

}