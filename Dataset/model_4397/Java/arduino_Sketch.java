





import java.util.List;
import java.util.ArrayList;

public class arduino_Sketch extends NamedElement {






    private arduino_Project arduino_project;




    private arduino_Block arduino_block;


    public arduino_Sketch(
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
    public arduino_Block getArduino_block() {
        return arduino_block;
    }

    public void setArduino_block(arduino_Block arduino_block) {
        this.arduino_block = arduino_block;
    }

}