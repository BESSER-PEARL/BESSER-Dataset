





import java.util.List;
import java.util.ArrayList;

public class whileDsl_Exprs  {






    private whileDsl_VarsCommand whiledsl_varscommand;




    private List<whileDsl_Expr> whiledsl_exprs;


    public whileDsl_Exprs(
    ) {
        this.whiledsl_exprs = new ArrayList<>();
    }

    public whileDsl_Exprs(
        ArrayList<whileDsl_Expr> whiledsl_exprs    ) {
        this.whiledsl_exprs = whiledsl_exprs;
    }


    public whileDsl_VarsCommand getWhiledsl_varscommand() {
        return whiledsl_varscommand;
    }

    public void setWhiledsl_varscommand(whileDsl_VarsCommand whiledsl_varscommand) {
        this.whiledsl_varscommand = whiledsl_varscommand;
    }
    public List<whileDsl_Expr> getWhiledsl_exprs() {
        return whiledsl_exprs;
    }

    public void addWhiledsl_expr(Whiledsl_expr whiledsl_expr) {
        this.whiledsl_exprs.add(whiledsl_expr);
    }

}