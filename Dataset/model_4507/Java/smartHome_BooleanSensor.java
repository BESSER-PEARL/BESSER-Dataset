





import java.util.List;
import java.util.ArrayList;

public class smartHome_BooleanSensor extends Sensor {

    private boolean value;



    public smartHome_BooleanSensor(
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