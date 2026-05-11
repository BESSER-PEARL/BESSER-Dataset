





import java.util.List;
import java.util.ArrayList;

public class paplj_Cast extends Expr {






    private paplj_Expr paplj_expr;




    private paplj_Type paplj_type;


    public paplj_Cast(
    ) {
        super(
        );
    }



    public paplj_Expr getPaplj_expr() {
        return paplj_expr;
    }

    public void setPaplj_expr(paplj_Expr paplj_expr) {
        this.paplj_expr = paplj_expr;
    }
    public paplj_Type getPaplj_type() {
        return paplj_type;
    }

    public void setPaplj_type(paplj_Type paplj_type) {
        this.paplj_type = paplj_type;
    }

}