





import java.util.List;
import java.util.ArrayList;

public class statemachine_IntLiteral extends Value {

    private int value;



    public statemachine_IntLiteral(
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