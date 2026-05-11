





import java.util.List;
import java.util.ArrayList;

public class b_IntLiteral extends LogicalExpr, Arg, Condition {

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