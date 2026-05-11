





import java.util.List;
import java.util.ArrayList;

public class arduino_Setup  {

    private String name;





    private arduino_Sketch arduino_sketch;


    public arduino_Setup(
        String name    ) {
        this.name = name;
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