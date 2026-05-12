





import java.util.List;
import java.util.ArrayList;

public class sqls_TableRef  {

    private String alias;





    private sqls_Select sqls_select;




    private sqls_ColumnRef sqls_columnref;




    private sqls_Table sqls_table;


    public sqls_TableRef(
        String alias    ) {
        this.alias = alias;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }

    public sqls_Select getSqls_select() {
        return sqls_select;
    }

    public void setSqls_select(sqls_Select sqls_select) {
        this.sqls_select = sqls_select;
    }
    public sqls_ColumnRef getSqls_columnref() {
        return sqls_columnref;
    }

    public void setSqls_columnref(sqls_ColumnRef sqls_columnref) {
        this.sqls_columnref = sqls_columnref;
    }
    public sqls_Table getSqls_table() {
        return sqls_table;
    }

    public void setSqls_table(sqls_Table sqls_table) {
        this.sqls_table = sqls_table;
    }

}