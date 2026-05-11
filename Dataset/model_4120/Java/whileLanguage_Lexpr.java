





import java.util.List;
import java.util.ArrayList;

public class whileLanguage_Lexpr  {






    private whileLanguage_Expr whilelanguage_expr;




    private List<whileLanguage_Expr> whilelanguage_exprs;


    public whileLanguage_Lexpr(
    ) {
        this.whilelanguage_exprs = new ArrayList<>();
    }

    public whileLanguage_Lexpr(
        ArrayList<whileLanguage_Expr> whilelanguage_exprs    ) {
        this.whilelanguage_exprs = whilelanguage_exprs;
    }


    public whileLanguage_Expr getWhilelanguage_expr() {
        return whilelanguage_expr;
    }

    public void setWhilelanguage_expr(whileLanguage_Expr whilelanguage_expr) {
        this.whilelanguage_expr = whilelanguage_expr;
    }
    public List<whileLanguage_Expr> getWhilelanguage_exprs() {
        return whilelanguage_exprs;
    }

    public void addWhilelanguage_expr(Whilelanguage_expr whilelanguage_expr) {
        this.whilelanguage_exprs.add(whilelanguage_expr);
    }

}