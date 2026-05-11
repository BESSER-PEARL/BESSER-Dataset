





import java.util.List;
import java.util.ArrayList;

public class smartHome_IntegerSensor extends Sensor {

    private int value;



    public smartHome_IntegerSensor(
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