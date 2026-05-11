





import java.util.List;
import java.util.ArrayList;

public class iot_MulOrDiv extends Expression {

    private String op;



    public iot_MulOrDiv(
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