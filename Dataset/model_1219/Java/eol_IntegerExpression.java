





import java.util.List;
import java.util.ArrayList;

public class eol_IntegerExpression extends PrimitiveExpression {

    private int val;



    public eol_IntegerExpression(
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