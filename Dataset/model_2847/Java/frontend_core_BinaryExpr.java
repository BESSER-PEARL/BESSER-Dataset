





import java.util.List;
import java.util.ArrayList;

public class frontend_core_BinaryExpr extends Expression {

    private String binaryOp;



    public frontend_core_BinaryExpr(
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