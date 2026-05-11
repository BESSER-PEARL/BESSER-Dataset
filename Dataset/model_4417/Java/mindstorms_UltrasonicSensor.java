





import java.util.List;
import java.util.ArrayList;

public class mindstorms_UltrasonicSensor extends Sensor {

    private float value;
    private String operator;



    public mindstorms_UltrasonicSensor(
        float value,        String operator    ) {
        super(
        );
        this.value = value;
        this.operator = operator;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }
    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }


}