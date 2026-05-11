





import java.util.List;
import java.util.ArrayList;

public class dom_RealExpression extends PrimitiveExpression {

    private float val;



    public dom_RealExpression(
        float val    ) {
        super(
        );
        this.val = val;
    }


    public float getVal() {
        return val;
    }

    public void setVal(float val) {
        this.val = val;
    }


}