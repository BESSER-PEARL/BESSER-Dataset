





import java.util.List;
import java.util.ArrayList;

public class smartHome_IntegerCondition extends Condition {

    private String operator;
    private int operand;





    private smartHome_IntegerSensor smarthome_integersensor;


    public smartHome_IntegerCondition(
        String operator,        int operand    ) {
        super(
        );
        this.operator = operator;
        this.operand = operand;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }
    public int getOperand() {
        return operand;
    }

    public void setOperand(int operand) {
        this.operand = operand;
    }

    public smartHome_IntegerSensor getSmarthome_integersensor() {
        return smarthome_integersensor;
    }

    public void setSmarthome_integersensor(smartHome_IntegerSensor smarthome_integersensor) {
        this.smarthome_integersensor = smarthome_integersensor;
    }

}