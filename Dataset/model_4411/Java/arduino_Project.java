





import java.util.List;
import java.util.ArrayList;

public class arduino_Project  {






    private List<arduino_Module> arduino_modules;




    private List<arduino_Sketch> arduino_sketchs;




    private arduino_Hardware arduino_hardware;




    private List<arduino_Platform> arduino_platforms;


    public arduino_Project(
    ) {
        this.arduino_modules = new ArrayList<>();
        this.arduino_sketchs = new ArrayList<>();
        this.arduino_platforms = new ArrayList<>();
    }

    public arduino_Project(
        ArrayList<arduino_Module> arduino_modules,        ArrayList<arduino_Sketch> arduino_sketchs,        ArrayList<arduino_Platform> arduino_platforms    ) {
        this.arduino_modules = arduino_modules;
        this.arduino_sketchs = arduino_sketchs;
        this.arduino_platforms = arduino_platforms;
    }


    public List<arduino_Module> getArduino_modules() {
        return arduino_modules;
    }

    public void addArduino_module(Arduino_module arduino_module) {
        this.arduino_modules.add(arduino_module);
    }
    public List<arduino_Sketch> getArduino_sketchs() {
        return arduino_sketchs;
    }

    public void addArduino_sketch(Arduino_sketch arduino_sketch) {
        this.arduino_sketchs.add(arduino_sketch);
    }
    public arduino_Hardware getArduino_hardware() {
        return arduino_hardware;
    }

    public void setArduino_hardware(arduino_Hardware arduino_hardware) {
        this.arduino_hardware = arduino_hardware;
    }
    public List<arduino_Platform> getArduino_platforms() {
        return arduino_platforms;
    }

    public void addArduino_platform(Arduino_platform arduino_platform) {
        this.arduino_platforms.add(arduino_platform);
    }

}