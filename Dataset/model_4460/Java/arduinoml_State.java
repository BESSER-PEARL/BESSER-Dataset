





import java.util.List;
import java.util.ArrayList;

public class arduinoml_State extends NamedElement {






    private arduinoml_App arduinoml_app;




    private List<arduinoml_Action> arduinoml_actions;


    public arduinoml_State(
    ) {
        super(
        );
        this.arduinoml_actions = new ArrayList<>();
    }

    public arduinoml_State(
        ArrayList<arduinoml_Action> arduinoml_actions    ) {
        this.arduinoml_actions = arduinoml_actions;
    }


    public arduinoml_App getArduinoml_app() {
        return arduinoml_app;
    }

    public void setArduinoml_app(arduinoml_App arduinoml_app) {
        this.arduinoml_app = arduinoml_app;
    }
    public List<arduinoml_Action> getArduinoml_actions() {
        return arduinoml_actions;
    }

    public void addArduinoml_action(Arduinoml_action arduinoml_action) {
        this.arduinoml_actions.add(arduinoml_action);
    }

}