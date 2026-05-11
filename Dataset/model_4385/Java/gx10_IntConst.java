





import java.util.List;
import java.util.ArrayList;

public class gx10_IntConst extends IntExpression {

    private int value;



    public gx10_IntConst(
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