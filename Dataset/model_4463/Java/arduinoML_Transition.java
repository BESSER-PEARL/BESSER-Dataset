





import java.util.List;
import java.util.ArrayList;

public class arduinoML_Transition  {






    private List<arduinoML_Condition> arduinoml_conditions;




    private arduinoML_State arduinoml_state;




    private arduinoML_State arduinoml_state;


    public arduinoML_Transition(
    ) {
        this.arduinoml_conditions = new ArrayList<>();
    }

    public arduinoML_Transition(
        ArrayList<arduinoML_Condition> arduinoml_conditions    ) {
        this.arduinoml_conditions = arduinoml_conditions;
    }


    public List<arduinoML_Condition> getArduinoml_conditions() {
        return arduinoml_conditions;
    }

    public void addArduinoml_condition(Arduinoml_condition arduinoml_condition) {
        this.arduinoml_conditions.add(arduinoml_condition);
    }
    public arduinoML_State getArduinoml_state() {
        return arduinoml_state;
    }

    public void setArduinoml_state(arduinoML_State arduinoml_state) {
        this.arduinoml_state = arduinoml_state;
    }
    public arduinoML_State getArduinoml_state() {
        return arduinoml_state;
    }

    public void setArduinoml_state(arduinoML_State arduinoml_state) {
        this.arduinoml_state = arduinoml_state;
    }

}