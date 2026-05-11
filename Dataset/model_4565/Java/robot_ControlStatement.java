





import java.util.List;
import java.util.ArrayList;

public class robot_ControlStatement extends Statement {

    private int value;



    public robot_ControlStatement(
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