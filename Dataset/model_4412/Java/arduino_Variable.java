





import java.util.List;
import java.util.ArrayList;

public class arduino_Variable extends Value, Instruction {

    private String name;





    private arduino_Set arduino_set;


    public arduino_Variable(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public arduino_Set getArduino_set() {
        return arduino_set;
    }

    public void setArduino_set(arduino_Set arduino_set) {
        this.arduino_set = arduino_set;
    }

}