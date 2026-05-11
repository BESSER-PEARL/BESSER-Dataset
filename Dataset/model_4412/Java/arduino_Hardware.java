





import java.util.List;
import java.util.ArrayList;

public class arduino_Hardware extends NamedElement {






    private arduino_Project arduino_project;




    private arduino_Sketch arduino_sketch;


    public arduino_Hardware(
    ) {
        super(
        );
    }



    public arduino_Project getArduino_project() {
        return arduino_project;
    }

    public void setArduino_project(arduino_Project arduino_project) {
        this.arduino_project = arduino_project;
    }
    public arduino_Sketch getArduino_sketch() {
        return arduino_sketch;
    }

    public void setArduino_sketch(arduino_Sketch arduino_sketch) {
        this.arduino_sketch = arduino_sketch;
    }

}