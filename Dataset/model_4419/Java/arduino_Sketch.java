





import java.util.List;
import java.util.ArrayList;

public class arduino_Sketch  {

    private String name;
    private boolean defineSystem;
    private String hardware;





    private List<arduino_AbstractDevice> arduino_abstractdevices;




    private List<arduino_Handler> arduino_handlers;


    public arduino_Sketch(
        String name,        boolean defineSystem,        String hardware    ) {
        this.name = name;
        this.defineSystem = defineSystem;
        this.hardware = hardware;
        this.arduino_abstractdevices = new ArrayList<>();
        this.arduino_handlers = new ArrayList<>();
    }

    public arduino_Sketch(
        String name,        boolean defineSystem,        String hardware        ArrayList<arduino_AbstractDevice> arduino_abstractdevices,        ArrayList<arduino_Handler> arduino_handlers    ) {
        this.name = name;
        this.defineSystem = defineSystem;
        this.hardware = hardware;
        this.arduino_abstractdevices = arduino_abstractdevices;
        this.arduino_handlers = arduino_handlers;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getDefinesystem() {
        return defineSystem;
    }

    public void setDefinesystem(boolean defineSystem) {
        this.defineSystem = defineSystem;
    }
    public String getHardware() {
        return hardware;
    }

    public void setHardware(String hardware) {
        this.hardware = hardware;
    }

    public List<arduino_AbstractDevice> getArduino_abstractdevices() {
        return arduino_abstractdevices;
    }

    public void addArduino_abstractdevice(Arduino_abstractdevice arduino_abstractdevice) {
        this.arduino_abstractdevices.add(arduino_abstractdevice);
    }
    public List<arduino_Handler> getArduino_handlers() {
        return arduino_handlers;
    }

    public void addArduino_handler(Arduino_handler arduino_handler) {
        this.arduino_handlers.add(arduino_handler);
    }

}