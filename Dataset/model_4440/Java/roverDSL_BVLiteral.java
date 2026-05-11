





import java.util.List;
import java.util.ArrayList;

public class roverDSL_BVLiteral extends ValueExpression {

    private boolean neg;
    private int aValue;



    public roverDSL_BVLiteral(
        boolean neg,        int aValue    ) {
        super(
        );
        this.neg = neg;
        this.aValue = aValue;
    }


    public boolean getNeg() {
        return neg;
    }

    public void setNeg(boolean neg) {
        this.neg = neg;
    }
    public int getAvalue() {
        return aValue;
    }

    public void setAvalue(int aValue) {
        this.aValue = aValue;
    }


}