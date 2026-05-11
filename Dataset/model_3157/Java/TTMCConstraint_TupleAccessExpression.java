





import java.util.List;
import java.util.ArrayList;

public class TTMCConstraint_TupleAccessExpression extends AccessExpression {

    private String index;



    public TTMCConstraint_TupleAccessExpression(
        String index    ) {
        super(
        );
        this.index = index;
    }


    public String getIndex() {
        return index;
    }

    public void setIndex(String index) {
        this.index = index;
    }


}