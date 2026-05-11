





import java.util.List;
import java.util.ArrayList;

public class b_IntLiteral extends Arg, Condition, LogicalExpr {

    private int value;



    public b_IntLiteral(
        int value    ) {
        super(
        );
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}