





import java.util.List;
import java.util.ArrayList;

public class smarthome_SensorPredicate extends Predicate {

    private String operator;
    private float value;





    private smarthome_Sensor smarthome_sensor;


    public smarthome_SensorPredicate(
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

    public smarthome_Sensor getSmarthome_sensor() {
        return smarthome_sensor;
    }

    public void setSmarthome_sensor(smarthome_Sensor smarthome_sensor) {
        this.smarthome_sensor = smarthome_sensor;
    }

}