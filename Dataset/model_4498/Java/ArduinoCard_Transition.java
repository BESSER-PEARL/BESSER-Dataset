





import java.util.List;
import java.util.ArrayList;

public class ArduinoCard_Transition  {

    private String name;





    private List<ArduinoCard_Condition> arduinocard_conditions;




    private ArduinoCard_State arduinocard_state;




    private ArduinoCard_Card arduinocard_card;




    private ArduinoCard_State arduinocard_state;


    public ArduinoCard_Transition(
        String name    ) {
        this.name = name;
        this.arduinocard_conditions = new ArrayList<>();
    }

    public ArduinoCard_Transition(
        String name        ArrayList<ArduinoCard_Condition> arduinocard_conditions    ) {
        this.name = name;
        this.arduinocard_conditions = arduinocard_conditions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ArduinoCard_Condition> getArduinocard_conditions() {
        return arduinocard_conditions;
    }

    public void addArduinocard_condition(Arduinocard_condition arduinocard_condition) {
        this.arduinocard_conditions.add(arduinocard_condition);
    }
    public ArduinoCard_State getArduinocard_state() {
        return arduinocard_state;
    }

    public void setArduinocard_state(ArduinoCard_State arduinocard_state) {
        this.arduinocard_state = arduinocard_state;
    }
    public ArduinoCard_Card getArduinocard_card() {
        return arduinocard_card;
    }

    public void setArduinocard_card(ArduinoCard_Card arduinocard_card) {
        this.arduinocard_card = arduinocard_card;
    }
    public ArduinoCard_State getArduinocard_state() {
        return arduinocard_state;
    }

    public void setArduinocard_state(ArduinoCard_State arduinocard_state) {
        this.arduinocard_state = arduinocard_state;
    }

}