





import java.util.List;
import java.util.ArrayList;

public class b_Values  {






    private b_Implementation b_implementation;




    private List<b_ValueExpr> b_valueexprs;


    public b_Values(
    ) {
        this.b_valueexprs = new ArrayList<>();
    }

    public b_Values(
        ArrayList<b_ValueExpr> b_valueexprs    ) {
        this.b_valueexprs = b_valueexprs;
    }


    public b_Implementation getB_implementation() {
        return b_implementation;
    }

    public void setB_implementation(b_Implementation b_implementation) {
        this.b_implementation = b_implementation;
    }
    public List<b_ValueExpr> getB_valueexprs() {
        return b_valueexprs;
    }

    public void addB_valueexpr(B_valueexpr b_valueexpr) {
        this.b_valueexprs.add(b_valueexpr);
    }

}