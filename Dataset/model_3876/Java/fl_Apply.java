





import java.util.List;
import java.util.ArrayList;

public class fl_Apply extends Expr {

    private String name;





    private List<fl_Expr> fl_exprs;


    public fl_Apply(
        String name    ) {
        super(
        );
        this.name = name;
        this.fl_exprs = new ArrayList<>();
    }

    public fl_Apply(
        String name        ArrayList<fl_Expr> fl_exprs    ) {
        this.name = name;
        this.fl_exprs = fl_exprs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<fl_Expr> getFl_exprs() {
        return fl_exprs;
    }

    public void addFl_expr(Fl_expr fl_expr) {
        this.fl_exprs.add(fl_expr);
    }

}