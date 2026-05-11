





import java.util.List;
import java.util.ArrayList;

public class arduino_BooleanConstant extends Constant, BooleanExpression {

    private boolean value;



    public arduino_BooleanConstant(
        boolean value    ) {
        super(
        );
        this.value = value;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }


}