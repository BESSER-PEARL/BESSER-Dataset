





import java.util.List;
import java.util.ArrayList;

public class boa_EvalFunRes extends EvalRes {

    private String name;





    private boa_Ctx boa_ctx;




    private boa_Expr boa_expr;


    public boa_EvalFunRes(
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

    public boa_Ctx getBoa_ctx() {
        return boa_ctx;
    }

    public void setBoa_ctx(boa_Ctx boa_ctx) {
        this.boa_ctx = boa_ctx;
    }
    public boa_Expr getBoa_expr() {
        return boa_expr;
    }

    public void setBoa_expr(boa_Expr boa_expr) {
        this.boa_expr = boa_expr;
    }

}