





import java.util.List;
import java.util.ArrayList;

public class paplj_Let extends Expr {






    private List<paplj_Binding> paplj_bindings;




    private paplj_Expr paplj_expr;


    public paplj_Let(
    ) {
        super(
        );
        this.paplj_bindings = new ArrayList<>();
    }

    public paplj_Let(
        ArrayList<paplj_Binding> paplj_bindings    ) {
        this.paplj_bindings = paplj_bindings;
    }


    public List<paplj_Binding> getPaplj_bindings() {
        return paplj_bindings;
    }

    public void addPaplj_binding(Paplj_binding paplj_binding) {
        this.paplj_bindings.add(paplj_binding);
    }
    public paplj_Expr getPaplj_expr() {
        return paplj_expr;
    }

    public void setPaplj_expr(paplj_Expr paplj_expr) {
        this.paplj_expr = paplj_expr;
    }

}