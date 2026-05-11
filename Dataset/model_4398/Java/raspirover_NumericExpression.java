





import java.util.List;
import java.util.ArrayList;

public class raspirover_NumericExpression extends RoverExpression {

    private boolean op;



    public raspirover_NumericExpression(
        boolean op    ) {
        super(
        );
        this.op = op;
    }


    public boolean getOp() {
        return op;
    }

    public void setOp(boolean op) {
        this.op = op;
    }


}