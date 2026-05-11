





import java.util.List;
import java.util.ArrayList;

public class calculatrice_Number extends CalcExpr {

    private boolean neg;
    private int value;



    public calculatrice_Number(
        boolean neg,        int value    ) {
        super(
        );
        this.neg = neg;
        this.value = value;
    }


    public boolean getNeg() {
        return neg;
    }

    public void setNeg(boolean neg) {
        this.neg = neg;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}