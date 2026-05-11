





import java.util.List;
import java.util.ArrayList;

public class expression_IntegerLiteral extends Literal {

    private int val;



    public expression_IntegerLiteral(
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