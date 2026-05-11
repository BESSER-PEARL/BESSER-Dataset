





import java.util.List;
import java.util.ArrayList;

public class jkind_NodeCallExpr extends Expr {






    private jkind_Node jkind_node;




    private List<jkind_Expr> jkind_exprs;


    public jkind_NodeCallExpr(
    ) {
        super(
        );
        this.jkind_exprs = new ArrayList<>();
    }

    public jkind_NodeCallExpr(
        ArrayList<jkind_Expr> jkind_exprs    ) {
        this.jkind_exprs = jkind_exprs;
    }


    public jkind_Node getJkind_node() {
        return jkind_node;
    }

    public void setJkind_node(jkind_Node jkind_node) {
        this.jkind_node = jkind_node;
    }
    public List<jkind_Expr> getJkind_exprs() {
        return jkind_exprs;
    }

    public void addJkind_expr(Jkind_expr jkind_expr) {
        this.jkind_exprs.add(jkind_expr);
    }

}