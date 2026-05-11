





import java.util.List;
import java.util.ArrayList;

public class expressionDSL_IntConstant extends Expression {

    private int value;



    public expressionDSL_IntConstant(
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