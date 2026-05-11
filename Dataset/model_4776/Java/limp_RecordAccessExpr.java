





import java.util.List;
import java.util.ArrayList;

public class limp_RecordAccessExpr extends Expr {

    private String field;





    private limp_Expr limp_expr;


    public limp_RecordAccessExpr(
        String field    ) {
        super(
        );
        this.field = field;
    }


    public String getField() {
        return field;
    }

    public void setField(String field) {
        this.field = field;
    }

    public limp_Expr getLimp_expr() {
        return limp_expr;
    }

    public void setLimp_expr(limp_Expr limp_expr) {
        this.limp_expr = limp_expr;
    }

}