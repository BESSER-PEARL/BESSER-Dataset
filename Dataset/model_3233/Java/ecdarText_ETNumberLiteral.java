





import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETNumberLiteral extends ETExpression {

    private int value;



    public ecdarText_ETNumberLiteral(
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