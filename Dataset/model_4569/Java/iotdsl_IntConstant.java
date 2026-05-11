





import java.util.List;
import java.util.ArrayList;

public class iotdsl_IntConstant extends Value {

    private int value;



    public iotdsl_IntConstant(
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