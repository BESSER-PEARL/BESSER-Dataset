





import java.util.List;
import java.util.ArrayList;

public class arduino_Block  {






    private arduino_Sketch arduino_sketch;




    private arduino_Control arduino_control;


    public arduino_Block(
    ) {
    }



    public arduino_Sketch getArduino_sketch() {
        return arduino_sketch;
    }

    public void setArduino_sketch(arduino_Sketch arduino_sketch) {
        this.arduino_sketch = arduino_sketch;
    }
    public arduino_Control getArduino_control() {
        return arduino_control;
    }

    public void setArduino_control(arduino_Control arduino_control) {
        this.arduino_control = arduino_control;
    }

}