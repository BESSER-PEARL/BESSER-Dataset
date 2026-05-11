





import java.util.List;
import java.util.ArrayList;

public class mathInterpreter_Div extends Exp {

    private String op;



    public mathInterpreter_Div(
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