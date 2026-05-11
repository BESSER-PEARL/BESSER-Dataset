





import java.util.List;
import java.util.ArrayList;

public class langage_while_LExpr  {






    private List<langage_while_Expr> langage_while_exprs;


    public langage_while_LExpr(
    ) {
        this.langage_while_exprs = new ArrayList<>();
    }

    public langage_while_LExpr(
        ArrayList<langage_while_Expr> langage_while_exprs    ) {
        this.langage_while_exprs = langage_while_exprs;
    }


    public List<langage_while_Expr> getLangage_while_exprs() {
        return langage_while_exprs;
    }

    public void addLangage_while_expr(Langage_while_expr langage_while_expr) {
        this.langage_while_exprs.add(langage_while_expr);
    }

}