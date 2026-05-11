





import java.util.List;
import java.util.ArrayList;

public class arduino_Interrupt  {

    private String interruptKind;
    private String eventKind;
    private String name;





    private arduino_Handler arduino_handler;


    public arduino_Interrupt(
        String interruptKind,        String eventKind,        String name    ) {
        this.interruptKind = interruptKind;
        this.eventKind = eventKind;
        this.name = name;
    }


    public String getInterruptkind() {
        return interruptKind;
    }

    public void setInterruptkind(String interruptKind) {
        this.interruptKind = interruptKind;
    }
    public String getEventkind() {
        return eventKind;
    }

    public void setEventkind(String eventKind) {
        this.eventKind = eventKind;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public arduino_Handler getArduino_handler() {
        return arduino_handler;
    }

    public void setArduino_handler(arduino_Handler arduino_handler) {
        this.arduino_handler = arduino_handler;
    }

}