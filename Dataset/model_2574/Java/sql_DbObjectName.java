





import java.util.List;
import java.util.ArrayList;

public class sql_DbObjectName extends TableFull, ColumnFull, PivotCol, UsingCols {

    private String dbname;





    private sql_pcols sql_pcols;




    private sql_tbls sql_tbls;




    private sql_Col sql_col;




    private sql_AnalyticExprArg sql_analyticexprarg;




    private sql_ColumnOrAlias sql_columnoralias;


    public sql_DbObjectName(
        String dbname    ) {
        super(
        );
        this.dbname = dbname;
    }


    public String getDbname() {
        return dbname;
    }

    public void setDbname(String dbname) {
        this.dbname = dbname;
    }

    public sql_pcols getSql_pcols() {
        return sql_pcols;
    }

    public void setSql_pcols(sql_pcols sql_pcols) {
        this.sql_pcols = sql_pcols;
    }
    public sql_tbls getSql_tbls() {
        return sql_tbls;
    }

    public void setSql_tbls(sql_tbls sql_tbls) {
        this.sql_tbls = sql_tbls;
    }
    public sql_Col getSql_col() {
        return sql_col;
    }

    public void setSql_col(sql_Col sql_col) {
        this.sql_col = sql_col;
    }
    public sql_AnalyticExprArg getSql_analyticexprarg() {
        return sql_analyticexprarg;
    }

    public void setSql_analyticexprarg(sql_AnalyticExprArg sql_analyticexprarg) {
        this.sql_analyticexprarg = sql_analyticexprarg;
    }
    public sql_ColumnOrAlias getSql_columnoralias() {
        return sql_columnoralias;
    }

    public void setSql_columnoralias(sql_ColumnOrAlias sql_columnoralias) {
        this.sql_columnoralias = sql_columnoralias;
    }

}