





import java.util.List;
import java.util.ArrayList;

public class smartHome_BooleanCondition extends Condition {

    private String operator;
    private boolean operand;





    private smartHome_BooleanSensor smarthome_booleansensor;


    public smartHome_BooleanCondition(
        String operator,        boolean operand    ) {
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
    public boolean getOperand() {
        return operand;
    }

    public void setOperand(boolean operand) {
        this.operand = operand;
    }

    public smartHome_BooleanSensor getSmarthome_booleansensor() {
        return smarthome_booleansensor;
    }

    public void setSmarthome_booleansensor(smartHome_BooleanSensor smarthome_booleansensor) {
        this.smarthome_booleansensor = smarthome_booleansensor;
    }

}