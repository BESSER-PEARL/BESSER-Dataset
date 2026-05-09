





import java.util.List;
import java.util.ArrayList;

public class SimplStateMachine_BooleanData extends Data {

    private boolean value;



    public SimplStateMachine_BooleanData(
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