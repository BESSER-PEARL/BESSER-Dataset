





import java.util.List;
import java.util.ArrayList;

public class arduinoml_AnalogActionValue extends AnalogAction {

    private int value;



    public arduinoml_AnalogActionValue(
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