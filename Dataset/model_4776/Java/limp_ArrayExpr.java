





import java.util.List;
import java.util.ArrayList;

public class limp_ArrayExpr extends Expr {






    private limp_ArrayTypeDef limp_arraytypedef;




    private List<limp_Expr> limp_exprs;


    public limp_ArrayExpr(
    ) {
        super(
        );
        this.limp_exprs = new ArrayList<>();
    }

    public limp_ArrayExpr(
        ArrayList<limp_Expr> limp_exprs    ) {
        this.limp_exprs = limp_exprs;
    }


    public limp_ArrayTypeDef getLimp_arraytypedef() {
        return limp_arraytypedef;
    }

    public void setLimp_arraytypedef(limp_ArrayTypeDef limp_arraytypedef) {
        this.limp_arraytypedef = limp_arraytypedef;
    }
    public List<limp_Expr> getLimp_exprs() {
        return limp_exprs;
    }

    public void addLimp_expr(Limp_expr limp_expr) {
        this.limp_exprs.add(limp_expr);
    }

}