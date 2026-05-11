





import java.util.List;
import java.util.ArrayList;

public class b_AndExpr extends LogicalExpr {






    private List<b_LogicalExpr> b_logicalexprs;


    public b_AndExpr(
    ) {
        super(
        );
        this.b_logicalexprs = new ArrayList<>();
    }

    public b_AndExpr(
        ArrayList<b_LogicalExpr> b_logicalexprs    ) {
        this.b_logicalexprs = b_logicalexprs;
    }


    public List<b_LogicalExpr> getB_logicalexprs() {
        return b_logicalexprs;
    }

    public void addB_logicalexpr(B_logicalexpr b_logicalexpr) {
        this.b_logicalexprs.add(b_logicalexpr);
    }

}