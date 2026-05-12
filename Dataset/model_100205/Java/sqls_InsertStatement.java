





import java.util.List;
import java.util.ArrayList;

public class sqls_InsertStatement extends SqlSentence {






    private sqls_Table sqls_table;




    private List<sqls_Column> sqls_columns;




    private List<sqls_SqlExpr> sqls_sqlexprs;


    public sqls_InsertStatement(
    ) {
        super(
        );
        this.sqls_columns = new ArrayList<>();
        this.sqls_sqlexprs = new ArrayList<>();
    }

    public sqls_InsertStatement(
        ArrayList<sqls_Column> sqls_columns,        ArrayList<sqls_SqlExpr> sqls_sqlexprs    ) {
        this.sqls_columns = sqls_columns;
        this.sqls_sqlexprs = sqls_sqlexprs;
    }


    public sqls_Table getSqls_table() {
        return sqls_table;
    }

    public void setSqls_table(sqls_Table sqls_table) {
        this.sqls_table = sqls_table;
    }
    public List<sqls_Column> getSqls_columns() {
        return sqls_columns;
    }

    public void addSqls_column(Sqls_column sqls_column) {
        this.sqls_columns.add(sqls_column);
    }
    public List<sqls_SqlExpr> getSqls_sqlexprs() {
        return sqls_sqlexprs;
    }

    public void addSqls_sqlexpr(Sqls_sqlexpr sqls_sqlexpr) {
        this.sqls_sqlexprs.add(sqls_sqlexpr);
    }

}