





import java.util.List;
import java.util.ArrayList;

public class core_BinaryExpr extends Expression {

    private String binaryOp;



    public core_BinaryExpr(
        String binaryOp    ) {
        super(
        );
        this.binaryOp = binaryOp;
    }


    public String getBinaryop() {
        return binaryOp;
    }

    public void setBinaryop(String binaryOp) {
        this.binaryOp = binaryOp;
    }


}