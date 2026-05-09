





import java.util.List;
import java.util.ArrayList;

public class gfsm_ConstExpr extends IntExpression {

    private int value;



    public gfsm_ConstExpr(
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