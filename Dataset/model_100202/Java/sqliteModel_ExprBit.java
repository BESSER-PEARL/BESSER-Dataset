





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_ExprBit extends Expression {

    private String op;



    public sqliteModel_ExprBit(
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