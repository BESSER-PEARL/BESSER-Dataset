





import java.util.List;
import java.util.ArrayList;

public class arduino_Board extends NamedElement {






    private arduino_Sketch arduino_sketch;


    public arduino_Board(
    ) {
        super(
        );
    }



    public arduino_Sketch getArduino_sketch() {
        return arduino_sketch;
    }

    public void setArduino_sketch(arduino_Sketch arduino_sketch) {
        this.arduino_sketch = arduino_sketch;
    }

}