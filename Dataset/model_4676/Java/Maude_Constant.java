





import java.util.List;
import java.util.ArrayList;

public class Maude_Constant extends Term {

    private String op;



    public Maude_Constant(
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