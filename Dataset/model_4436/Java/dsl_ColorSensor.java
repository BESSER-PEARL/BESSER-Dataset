





import java.util.List;
import java.util.ArrayList;

public class dsl_ColorSensor extends SensorType {

    private String key;



    public dsl_ColorSensor(
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