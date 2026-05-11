





import java.util.List;
import java.util.ArrayList;

public class arduino_Board extends NamedElement {






    private List<arduino_Module> arduino_modules;




    private arduino_Project arduino_project;


    public arduino_Board(
    ) {
        super(
        );
        this.arduino_modules = new ArrayList<>();
    }

    public arduino_Board(
        ArrayList<arduino_Module> arduino_modules    ) {
        this.arduino_modules = arduino_modules;
    }


    public List<arduino_Module> getArduino_modules() {
        return arduino_modules;
    }

    public void addArduino_module(Arduino_module arduino_module) {
        this.arduino_modules.add(arduino_module);
    }
    public arduino_Project getArduino_project() {
        return arduino_project;
    }

    public void setArduino_project(arduino_Project arduino_project) {
        this.arduino_project = arduino_project;
    }

}