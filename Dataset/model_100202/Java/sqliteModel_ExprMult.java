





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_ExprMult extends Expression {

    private String op;



    public sqliteModel_ExprMult(
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