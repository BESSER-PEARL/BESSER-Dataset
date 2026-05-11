





import java.util.List;
import java.util.ArrayList;

public class behaviour_IntConstantExpression extends ConstantExpression {

    private int value;



    public behaviour_IntConstantExpression(
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