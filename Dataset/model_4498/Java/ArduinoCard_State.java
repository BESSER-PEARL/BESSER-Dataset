





import java.util.List;
import java.util.ArrayList;

public class ArduinoCard_State  {

    private boolean isInitial;
    private String name;





    private List<ArduinoCard_Command> arduinocard_commands;




    private ArduinoCard_Card arduinocard_card;


    public ArduinoCard_State(
        boolean isInitial,        String name    ) {
        this.isInitial = isInitial;
        this.name = name;
        this.arduinocard_commands = new ArrayList<>();
    }

    public ArduinoCard_State(
        boolean isInitial,        String name        ArrayList<ArduinoCard_Command> arduinocard_commands    ) {
        this.isInitial = isInitial;
        this.name = name;
        this.arduinocard_commands = arduinocard_commands;
    }

    public boolean getIsinitial() {
        return isInitial;
    }

    public void setIsinitial(boolean isInitial) {
        this.isInitial = isInitial;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ArduinoCard_Command> getArduinocard_commands() {
        return arduinocard_commands;
    }

    public void addArduinocard_command(Arduinocard_command arduinocard_command) {
        this.arduinocard_commands.add(arduinocard_command);
    }
    public ArduinoCard_Card getArduinocard_card() {
        return arduinocard_card;
    }

    public void setArduinocard_card(ArduinoCard_Card arduinocard_card) {
        this.arduinocard_card = arduinocard_card;
    }

}