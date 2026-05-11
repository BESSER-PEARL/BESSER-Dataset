





import java.util.List;
import java.util.ArrayList;

public class rcl_StringExpression extends RoverExpression {

    private boolean op;



    public rcl_StringExpression(
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