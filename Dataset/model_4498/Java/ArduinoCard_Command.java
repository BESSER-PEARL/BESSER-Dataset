





import java.util.List;
import java.util.ArrayList;

public class ArduinoCard_Command extends BlockInteraction {






    private ArduinoCard_Actuator arduinocard_actuator;


    public ArduinoCard_Command(
    ) {
        super(
        );
    }



    public ArduinoCard_Actuator getArduinocard_actuator() {
        return arduinocard_actuator;
    }

    public void setArduinocard_actuator(ArduinoCard_Actuator arduinocard_actuator) {
        this.arduinocard_actuator = arduinocard_actuator;
    }

}