





import java.util.List;
import java.util.ArrayList;

public class arduinoml_MultipleElementCondition extends Condition {

    private String operators;





    private arduinoml_Transition arduinoml_transition;


    public arduinoml_MultipleElementCondition(
        String operators    ) {
        super(
        );
        this.operators = operators;
    }


    public String getOperators() {
        return operators;
    }

    public void setOperators(String operators) {
        this.operators = operators;
    }

    public arduinoml_Transition getArduinoml_transition() {
        return arduinoml_transition;
    }

    public void setArduinoml_transition(arduinoml_Transition arduinoml_transition) {
        this.arduinoml_transition = arduinoml_transition;
    }

}