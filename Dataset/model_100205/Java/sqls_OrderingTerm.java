





import java.util.List;
import java.util.ArrayList;

public class sqls_OrderingTerm  {

    private boolean desc;
    private boolean asc;





    private sqls_Select sqls_select;




    private sqls_SqlExpr sqls_sqlexpr;


    public sqls_OrderingTerm(
        boolean desc,        boolean asc    ) {
        this.desc = desc;
        this.asc = asc;
    }


    public boolean getDesc() {
        return desc;
    }

    public void setDesc(boolean desc) {
        this.desc = desc;
    }
    public boolean getAsc() {
        return asc;
    }

    public void setAsc(boolean asc) {
        this.asc = asc;
    }

    public sqls_Select getSqls_select() {
        return sqls_select;
    }

    public void setSqls_select(sqls_Select sqls_select) {
        this.sqls_select = sqls_select;
    }
    public sqls_SqlExpr getSqls_sqlexpr() {
        return sqls_sqlexpr;
    }

    public void setSqls_sqlexpr(sqls_SqlExpr sqls_sqlexpr) {
        this.sqls_sqlexpr = sqls_sqlexpr;
    }

}