





import java.util.List;
import java.util.ArrayList;

public class imp_Var extends Expr {

    private String name;





    private imp_Expr imp_expr;


    public imp_Var(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public imp_Expr getImp_expr() {
        return imp_expr;
    }

    public void setImp_expr(imp_Expr imp_expr) {
        this.imp_expr = imp_expr;
    }

}