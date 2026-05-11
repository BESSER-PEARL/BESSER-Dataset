





import java.util.List;
import java.util.ArrayList;

public class b_InequalityExpr extends LogicalExpr {

    private String op;



    public b_InequalityExpr(
        String op    ) {
        super(
        );
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }


}