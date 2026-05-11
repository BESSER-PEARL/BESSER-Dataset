





import java.util.List;
import java.util.ArrayList;

public class imp_Unary extends Expr {

    private String op;



    public imp_Unary(
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