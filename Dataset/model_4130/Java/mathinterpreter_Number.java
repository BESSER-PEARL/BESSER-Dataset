





import java.util.List;
import java.util.ArrayList;

public class mathinterpreter_Number extends Primary {

    private int value;



    public mathinterpreter_Number(
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