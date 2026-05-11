





import java.util.List;
import java.util.ArrayList;

public class smartHome_Condition  {

    private int operand;
    private String operator;





    private smartHome_Rule smarthome_rule;




    private smartHome_Sensor smarthome_sensor;


    public smartHome_Condition(
        int operand,        String operator    ) {
        this.operand = operand;
        this.operator = operator;
    }


    public int getOperand() {
        return operand;
    }

    public void setOperand(int operand) {
        this.operand = operand;
    }
    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public smartHome_Rule getSmarthome_rule() {
        return smarthome_rule;
    }

    public void setSmarthome_rule(smartHome_Rule smarthome_rule) {
        this.smarthome_rule = smarthome_rule;
    }
    public smartHome_Sensor getSmarthome_sensor() {
        return smarthome_sensor;
    }

    public void setSmarthome_sensor(smartHome_Sensor smarthome_sensor) {
        this.smarthome_sensor = smarthome_sensor;
    }

}