





import java.util.List;
import java.util.ArrayList;

public class oogen_OOIntegerLiteral extends OOArithmeticExpression {

    private int value;



    public oogen_OOIntegerLiteral(
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