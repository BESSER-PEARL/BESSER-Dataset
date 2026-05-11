





import java.util.List;
import java.util.ArrayList;

public class sql_ColumnOrAlias extends OrColumn {

    private String alias;
    private String allCols;





    private sql_DbObjectName sql_dbobjectname;




    private sql_OrColumn sql_orcolumn;




    private sql_Operands sql_operands;


    public sql_ColumnOrAlias(
        String alias,        String allCols    ) {
        super(
        );
        this.alias = alias;
        this.allCols = allCols;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public String getAllcols() {
        return allCols;
    }

    public void setAllcols(String allCols) {
        this.allCols = allCols;
    }

    public sql_DbObjectName getSql_dbobjectname() {
        return sql_dbobjectname;
    }

    public void setSql_dbobjectname(sql_DbObjectName sql_dbobjectname) {
        this.sql_dbobjectname = sql_dbobjectname;
    }
    public sql_OrColumn getSql_orcolumn() {
        return sql_orcolumn;
    }

    public void setSql_orcolumn(sql_OrColumn sql_orcolumn) {
        this.sql_orcolumn = sql_orcolumn;
    }
    public sql_Operands getSql_operands() {
        return sql_operands;
    }

    public void setSql_operands(sql_Operands sql_operands) {
        this.sql_operands = sql_operands;
    }

}