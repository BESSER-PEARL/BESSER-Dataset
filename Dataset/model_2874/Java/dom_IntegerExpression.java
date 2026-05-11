





import java.util.List;
import java.util.ArrayList;

public class dom_IntegerExpression extends PrimitiveExpression {

    private int val;



    public dom_IntegerExpression(
        int val    ) {
        super(
        );
        this.val = val;
    }


    public int getVal() {
        return val;
    }

    public void setVal(int val) {
        this.val = val;
    }


}