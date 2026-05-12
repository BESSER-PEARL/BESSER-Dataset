





import java.util.List;
import java.util.ArrayList;

public class sqls_ResultColumn  {

    private String name;





    private sqls_SqlExpr sqls_sqlexpr;


    public sqls_ResultColumn(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sqls_SqlExpr getSqls_sqlexpr() {
        return sqls_sqlexpr;
    }

    public void setSqls_sqlexpr(sqls_SqlExpr sqls_sqlexpr) {
        this.sqls_sqlexpr = sqls_sqlexpr;
    }

}