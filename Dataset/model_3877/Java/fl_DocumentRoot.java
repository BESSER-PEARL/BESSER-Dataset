





import java.util.List;
import java.util.ArrayList;

public class fl_DocumentRoot  {

    private String mixed;





    private List<fl_Expr> fl_exprs;


    public fl_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.fl_exprs = new ArrayList<>();
    }

    public fl_DocumentRoot(
        String mixed        ArrayList<fl_Expr> fl_exprs    ) {
        this.mixed = mixed;
        this.fl_exprs = fl_exprs;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<fl_Expr> getFl_exprs() {
        return fl_exprs;
    }

    public void addFl_expr(Fl_expr fl_expr) {
        this.fl_exprs.add(fl_expr);
    }

}