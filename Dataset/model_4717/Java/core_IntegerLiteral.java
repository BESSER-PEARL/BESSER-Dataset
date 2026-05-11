





import java.util.List;
import java.util.ArrayList;

public class core_IntegerLiteral extends IntegerExpression {

    private int val;



    public core_IntegerLiteral(
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