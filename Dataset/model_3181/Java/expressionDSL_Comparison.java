





import java.util.List;
import java.util.ArrayList;

public class expressionDSL_Comparison extends Expression {

    private String op;



    public expressionDSL_Comparison(
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