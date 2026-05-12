





import java.util.List;
import java.util.ArrayList;

public class sqls_SqlFunction extends SqlExpr {






    private List<sqls_SqlExpr> sqls_sqlexprs;


    public sqls_SqlFunction(
    ) {
        super(
        );
        this.sqls_sqlexprs = new ArrayList<>();
    }

    public sqls_SqlFunction(
        ArrayList<sqls_SqlExpr> sqls_sqlexprs    ) {
        this.sqls_sqlexprs = sqls_sqlexprs;
    }


    public List<sqls_SqlExpr> getSqls_sqlexprs() {
        return sqls_sqlexprs;
    }

    public void addSqls_sqlexpr(Sqls_sqlexpr sqls_sqlexpr) {
        this.sqls_sqlexprs.add(sqls_sqlexpr);
    }

}