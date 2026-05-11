





import java.util.List;
import java.util.ArrayList;

public class arduinoML_BooleanCondition extends Condition {

    private String operator;





    private arduinoML_Transition arduinoml_transition;




    private arduinoML_SinkError arduinoml_sinkerror;


    public arduinoML_BooleanCondition(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public arduinoML_Transition getArduinoml_transition() {
        return arduinoml_transition;
    }

    public void setArduinoml_transition(arduinoML_Transition arduinoml_transition) {
        this.arduinoml_transition = arduinoml_transition;
    }
    public arduinoML_SinkError getArduinoml_sinkerror() {
        return arduinoml_sinkerror;
    }

    public void setArduinoml_sinkerror(arduinoML_SinkError arduinoml_sinkerror) {
        this.arduinoml_sinkerror = arduinoml_sinkerror;
    }

}