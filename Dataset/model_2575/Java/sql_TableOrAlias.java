





import java.util.List;
import java.util.ArrayList;

public class sql_TableOrAlias  {

    private String alias;





    private sql_UnpivotTable sql_unpivottable;




    private sql_SubQueryOperand sql_subqueryoperand;




    private sql_TableFull sql_tablefull;




    private sql_FromTable sql_fromtable;




    private sql_PivotTable sql_pivottable;




    private sql_DbObjectName sql_dbobjectname;




    private sql_FromValues sql_fromvalues;


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

    public sql_UnpivotTable getSql_unpivottable() {
        return sql_unpivottable;
    }

    public void setSql_unpivottable(sql_UnpivotTable sql_unpivottable) {
        this.sql_unpivottable = sql_unpivottable;
    }
    public sql_SubQueryOperand getSql_subqueryoperand() {
        return sql_subqueryoperand;
    }

    public void setSql_subqueryoperand(sql_SubQueryOperand sql_subqueryoperand) {
        this.sql_subqueryoperand = sql_subqueryoperand;
    }
    public sql_TableFull getSql_tablefull() {
        return sql_tablefull;
    }

    public void setSql_tablefull(sql_TableFull sql_tablefull) {
        this.sql_tablefull = sql_tablefull;
    }
    public sql_FromTable getSql_fromtable() {
        return sql_fromtable;
    }

    public void setSql_fromtable(sql_FromTable sql_fromtable) {
        this.sql_fromtable = sql_fromtable;
    }
    public sql_PivotTable getSql_pivottable() {
        return sql_pivottable;
    }

    public void setSql_pivottable(sql_PivotTable sql_pivottable) {
        this.sql_pivottable = sql_pivottable;
    }
    public sql_DbObjectName getSql_dbobjectname() {
        return sql_dbobjectname;
    }

    public void setSql_dbobjectname(sql_DbObjectName sql_dbobjectname) {
        this.sql_dbobjectname = sql_dbobjectname;
    }
    public sql_FromValues getSql_fromvalues() {
        return sql_fromvalues;
    }

    public void setSql_fromvalues(sql_FromValues sql_fromvalues) {
        this.sql_fromvalues = sql_fromvalues;
    }

}