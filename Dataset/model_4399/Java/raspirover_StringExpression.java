





import java.util.List;
import java.util.ArrayList;

public class raspirover_StringExpression extends RoverExpression {

    private boolean op;



    public raspirover_StringExpression(
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