





import java.util.List;
import java.util.ArrayList;

public class jkind_RecordExpr extends Expr {






    private List<jkind_Expr> jkind_exprs;




    private List<jkind_Field> jkind_fields;


    public jkind_RecordExpr(
    ) {
        super(
        );
        this.jkind_exprs = new ArrayList<>();
        this.jkind_fields = new ArrayList<>();
    }

    public jkind_RecordExpr(
        ArrayList<jkind_Expr> jkind_exprs,        ArrayList<jkind_Field> jkind_fields    ) {
        this.jkind_exprs = jkind_exprs;
        this.jkind_fields = jkind_fields;
    }


    public List<jkind_Expr> getJkind_exprs() {
        return jkind_exprs;
    }

    public void addJkind_expr(Jkind_expr jkind_expr) {
        this.jkind_exprs.add(jkind_expr);
    }
    public List<jkind_Field> getJkind_fields() {
        return jkind_fields;
    }

    public void addJkind_field(Jkind_field jkind_field) {
        this.jkind_fields.add(jkind_field);
    }

}