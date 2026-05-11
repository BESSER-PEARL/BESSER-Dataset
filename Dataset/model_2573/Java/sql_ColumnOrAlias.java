





import java.util.List;
import java.util.ArrayList;

public class sql_ColumnOrAlias extends OrColumn {

    private String allCols;
    private String alias;





    private sql_OrColumn sql_orcolumn;


    public sql_ColumnOrAlias(
        String allCols,        String alias    ) {
        super(
        );
        this.allCols = allCols;
        this.alias = alias;
    }


    public String getAllcols() {
        return allCols;
    }

    public void setAllcols(String allCols) {
        this.allCols = allCols;
    }
    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }

    public sql_OrColumn getSql_orcolumn() {
        return sql_orcolumn;
    }

    public void setSql_orcolumn(sql_OrColumn sql_orcolumn) {
        this.sql_orcolumn = sql_orcolumn;
    }

}