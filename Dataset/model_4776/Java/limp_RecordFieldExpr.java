





import java.util.List;
import java.util.ArrayList;

public class limp_RecordFieldExpr  {

    private String fieldName;





    private limp_RecordExpr limp_recordexpr;




    private limp_Expr limp_expr;


    public limp_RecordFieldExpr(
        String fieldName    ) {
        this.fieldName = fieldName;
    }


    public String getFieldname() {
        return fieldName;
    }

    public void setFieldname(String fieldName) {
        this.fieldName = fieldName;
    }

    public limp_RecordExpr getLimp_recordexpr() {
        return limp_recordexpr;
    }

    public void setLimp_recordexpr(limp_RecordExpr limp_recordexpr) {
        this.limp_recordexpr = limp_recordexpr;
    }
    public limp_Expr getLimp_expr() {
        return limp_expr;
    }

    public void setLimp_expr(limp_Expr limp_expr) {
        this.limp_expr = limp_expr;
    }

}