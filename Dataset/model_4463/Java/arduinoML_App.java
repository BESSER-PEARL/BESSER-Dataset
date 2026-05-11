





import java.util.List;
import java.util.ArrayList;

public class arduinoML_App  {

    private String name;





    private arduinoML_State arduinoml_state;




    private List<arduinoML_State> arduinoml_states;




    private List<arduinoML_Brick> arduinoml_bricks;


    public arduinoML_App(
        String name    ) {
        this.name = name;
        this.arduinoml_states = new ArrayList<>();
        this.arduinoml_bricks = new ArrayList<>();
    }

    public arduinoML_App(
        String name        ArrayList<arduinoML_State> arduinoml_states,        ArrayList<arduinoML_Brick> arduinoml_bricks    ) {
        this.name = name;
        this.arduinoml_states = arduinoml_states;
        this.arduinoml_bricks = arduinoml_bricks;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public arduinoML_State getArduinoml_state() {
        return arduinoml_state;
    }

    public void setArduinoml_state(arduinoML_State arduinoml_state) {
        this.arduinoml_state = arduinoml_state;
    }
    public List<arduinoML_State> getArduinoml_states() {
        return arduinoml_states;
    }

    public void addArduinoml_state(Arduinoml_state arduinoml_state) {
        this.arduinoml_states.add(arduinoml_state);
    }
    public List<arduinoML_Brick> getArduinoml_bricks() {
        return arduinoml_bricks;
    }

    public void addArduinoml_brick(Arduinoml_brick arduinoml_brick) {
        this.arduinoml_bricks.add(arduinoml_brick);
    }

}