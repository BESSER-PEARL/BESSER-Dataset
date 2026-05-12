





import java.util.List;
import java.util.ArrayList;

public class sqls_Update extends SqlSentence {






    private sqls_Table sqls_table;




    private sqls_SqlExpr sqls_sqlexpr;


    public sqls_Update(
    ) {
        super(
        );
    }



    public sqls_Table getSqls_table() {
        return sqls_table;
    }

    public void setSqls_table(sqls_Table sqls_table) {
        this.sqls_table = sqls_table;
    }
    public sqls_SqlExpr getSqls_sqlexpr() {
        return sqls_sqlexpr;
    }

    public void setSqls_sqlexpr(sqls_SqlExpr sqls_sqlexpr) {
        this.sqls_sqlexpr = sqls_sqlexpr;
    }

}