





import java.util.List;
import java.util.ArrayList;

public class mathInterpreter_Mult extends Exp {

    private String op;



    public mathInterpreter_Mult(
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