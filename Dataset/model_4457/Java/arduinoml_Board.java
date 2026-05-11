





import java.util.List;
import java.util.ArrayList;

public class arduinoml_Board  {






    private List<arduinoml_Brick> arduinoml_bricks;




    private List<arduinoml_State> arduinoml_states;




    private arduinoml_State arduinoml_state;


    public arduinoml_Board(
    ) {
        this.arduinoml_bricks = new ArrayList<>();
        this.arduinoml_states = new ArrayList<>();
    }

    public arduinoml_Board(
        ArrayList<arduinoml_Brick> arduinoml_bricks,        ArrayList<arduinoml_State> arduinoml_states    ) {
        this.arduinoml_bricks = arduinoml_bricks;
        this.arduinoml_states = arduinoml_states;
    }


    public List<arduinoml_Brick> getArduinoml_bricks() {
        return arduinoml_bricks;
    }

    public void addArduinoml_brick(Arduinoml_brick arduinoml_brick) {
        this.arduinoml_bricks.add(arduinoml_brick);
    }
    public List<arduinoml_State> getArduinoml_states() {
        return arduinoml_states;
    }

    public void addArduinoml_state(Arduinoml_state arduinoml_state) {
        this.arduinoml_states.add(arduinoml_state);
    }
    public arduinoml_State getArduinoml_state() {
        return arduinoml_state;
    }

    public void setArduinoml_state(arduinoml_State arduinoml_state) {
        this.arduinoml_state = arduinoml_state;
    }

}