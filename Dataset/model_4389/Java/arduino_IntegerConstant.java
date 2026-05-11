





import java.util.List;
import java.util.ArrayList;

public class arduino_IntegerConstant extends IntegerExpression, Constant {

    private int value;



    public arduino_IntegerConstant(
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