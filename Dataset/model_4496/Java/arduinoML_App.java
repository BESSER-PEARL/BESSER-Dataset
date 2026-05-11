





import java.util.List;
import java.util.ArrayList;

public class arduinoML_App extends NamedElement {






    private List<arduinoML_Brick> arduinoml_bricks;


    public arduinoML_App(
    ) {
        super(
        );
        this.arduinoml_bricks = new ArrayList<>();
    }

    public arduinoML_App(
        ArrayList<arduinoML_Brick> arduinoml_bricks    ) {
        this.arduinoml_bricks = arduinoml_bricks;
    }


    public List<arduinoML_Brick> getArduinoml_bricks() {
        return arduinoml_bricks;
    }

    public void addArduinoml_brick(Arduinoml_brick arduinoml_brick) {
        this.arduinoml_bricks.add(arduinoml_brick);
    }

}