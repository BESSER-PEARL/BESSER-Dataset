





import java.util.List;
import java.util.ArrayList;

public class langage_while_ExprAnd  {






    private langage_while_ExprOr langage_while_expror;




    private List<langage_while_ExprOr> langage_while_exprors;




    private langage_while_Expr langage_while_expr;


    public langage_while_ExprAnd(
    ) {
        this.langage_while_exprors = new ArrayList<>();
    }

    public langage_while_ExprAnd(
        ArrayList<langage_while_ExprOr> langage_while_exprors    ) {
        this.langage_while_exprors = langage_while_exprors;
    }


    public langage_while_ExprOr getLangage_while_expror() {
        return langage_while_expror;
    }

    public void setLangage_while_expror(langage_while_ExprOr langage_while_expror) {
        this.langage_while_expror = langage_while_expror;
    }
    public List<langage_while_ExprOr> getLangage_while_exprors() {
        return langage_while_exprors;
    }

    public void addLangage_while_expror(Langage_while_expror langage_while_expror) {
        this.langage_while_exprors.add(langage_while_expror);
    }
    public langage_while_Expr getLangage_while_expr() {
        return langage_while_expr;
    }

    public void setLangage_while_expr(langage_while_Expr langage_while_expr) {
        this.langage_while_expr = langage_while_expr;
    }

}