





import java.util.List;
import java.util.ArrayList;

public class dsl_TouchSensor extends SensorType {

    private String key;



    public dsl_TouchSensor(
        String key    ) {
        super(
        );
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }


}