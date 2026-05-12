





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_ExprAnd extends Expression {

    private String op;



    public sqliteModel_ExprAnd(
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