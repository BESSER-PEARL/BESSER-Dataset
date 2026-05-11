





import java.util.List;
import java.util.ArrayList;

public class arduino_Task  {

    private boolean external;
    private String name;





    private arduino_Sketch arduino_sketch;


    public arduino_Task(
        boolean external,        String name    ) {
        this.external = external;
        this.name = name;
    }


    public boolean getExternal() {
        return external;
    }

    public void setExternal(boolean external) {
        this.external = external;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public arduino_Sketch getArduino_sketch() {
        return arduino_sketch;
    }

    public void setArduino_sketch(arduino_Sketch arduino_sketch) {
        this.arduino_sketch = arduino_sketch;
    }

}