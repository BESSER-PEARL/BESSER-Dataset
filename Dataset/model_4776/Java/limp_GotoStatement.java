





import java.util.List;
import java.util.ArrayList;

public class limp_GotoStatement extends Statement {






    private limp_Expr limp_expr;




    private limp_LabelStatement limp_labelstatement;


    public limp_GotoStatement(
    ) {
        super(
        );
    }



    public limp_Expr getLimp_expr() {
        return limp_expr;
    }

    public void setLimp_expr(limp_Expr limp_expr) {
        this.limp_expr = limp_expr;
    }
    public limp_LabelStatement getLimp_labelstatement() {
        return limp_labelstatement;
    }

    public void setLimp_labelstatement(limp_LabelStatement limp_labelstatement) {
        this.limp_labelstatement = limp_labelstatement;
    }

}