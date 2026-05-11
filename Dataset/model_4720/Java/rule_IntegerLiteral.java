





import java.util.List;
import java.util.ArrayList;

public class rule_IntegerLiteral extends IntegerExpression {

    private int val;



    public rule_IntegerLiteral(
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