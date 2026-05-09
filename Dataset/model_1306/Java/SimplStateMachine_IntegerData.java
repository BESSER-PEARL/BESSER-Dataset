





import java.util.List;
import java.util.ArrayList;

public class SimplStateMachine_IntegerData extends Data {

    private int value;



    public SimplStateMachine_IntegerData(
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