





import java.util.List;
import java.util.ArrayList;

public class b_ReturnOr extends ReturnTypeExpr {






    private List<b_ReturnTypeExpr> b_returntypeexprs;


    public b_ReturnOr(
    ) {
        super(
        );
        this.b_returntypeexprs = new ArrayList<>();
    }

    public b_ReturnOr(
        ArrayList<b_ReturnTypeExpr> b_returntypeexprs    ) {
        this.b_returntypeexprs = b_returntypeexprs;
    }


    public List<b_ReturnTypeExpr> getB_returntypeexprs() {
        return b_returntypeexprs;
    }

    public void addB_returntypeexpr(B_returntypeexpr b_returntypeexpr) {
        this.b_returntypeexprs.add(b_returntypeexpr);
    }

}