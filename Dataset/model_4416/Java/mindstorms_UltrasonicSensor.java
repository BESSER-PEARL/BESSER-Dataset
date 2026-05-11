





import java.util.List;
import java.util.ArrayList;

public class mindstorms_UltrasonicSensor extends Sensor {

    private String operator;
    private float value;



    public mindstorms_UltrasonicSensor(
        String operator,        float value    ) {
        super(
        );
        this.operator = operator;
        this.value = value;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }
    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }


}