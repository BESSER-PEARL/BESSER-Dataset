





import java.util.List;
import java.util.ArrayList;

public class myDsl_Operation extends Expression {

    private int value2;
    private String op;



    public myDsl_Operation(
        int value2,        String op    ) {
        super(
        );
        this.value2 = value2;
        this.op = op;
    }


    public int getValue2() {
        return value2;
    }

    public void setValue2(int value2) {
        this.value2 = value2;
    }
    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }


}