





import java.util.List;
import java.util.ArrayList;

public class arduino_Interrupt  {

    private String name;
    private String eventKind;
    private String interruptKind;





    private arduino_Sketch arduino_sketch;




    private arduino_Handler arduino_handler;


    public arduino_Interrupt(
        String name,        String eventKind,        String interruptKind    ) {
        this.name = name;
        this.eventKind = eventKind;
        this.interruptKind = interruptKind;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEventkind() {
        return eventKind;
    }

    public void setEventkind(String eventKind) {
        this.eventKind = eventKind;
    }
    public String getInterruptkind() {
        return interruptKind;
    }

    public void setInterruptkind(String interruptKind) {
        this.interruptKind = interruptKind;
    }

    public arduino_Sketch getArduino_sketch() {
        return arduino_sketch;
    }

    public void setArduino_sketch(arduino_Sketch arduino_sketch) {
        this.arduino_sketch = arduino_sketch;
    }
    public arduino_Handler getArduino_handler() {
        return arduino_handler;
    }

    public void setArduino_handler(arduino_Handler arduino_handler) {
        this.arduino_handler = arduino_handler;
    }

}