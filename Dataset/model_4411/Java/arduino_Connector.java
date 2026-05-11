





import java.util.List;
import java.util.ArrayList;

public class arduino_Connector  {






    private arduino_Module arduino_module;




    private arduino_Hardware arduino_hardware;


    public arduino_Connector(
    ) {
    }



    public arduino_Module getArduino_module() {
        return arduino_module;
    }

    public void setArduino_module(arduino_Module arduino_module) {
        this.arduino_module = arduino_module;
    }
    public arduino_Hardware getArduino_hardware() {
        return arduino_hardware;
    }

    public void setArduino_hardware(arduino_Hardware arduino_hardware) {
        this.arduino_hardware = arduino_hardware;
    }

}