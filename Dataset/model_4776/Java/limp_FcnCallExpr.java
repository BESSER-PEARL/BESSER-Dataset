





import java.util.List;
import java.util.ArrayList;

public class limp_FcnCallExpr extends Expr {






    private limp_FunctionRef limp_functionref;


    public limp_FcnCallExpr(
    ) {
        super(
        );
    }



    public limp_FunctionRef getLimp_functionref() {
        return limp_functionref;
    }

    public void setLimp_functionref(limp_FunctionRef limp_functionref) {
        this.limp_functionref = limp_functionref;
    }

}