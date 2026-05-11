





import java.util.List;
import java.util.ArrayList;

public class arduino_Sensor extends AbstractDevice {

    private boolean pullup;
    private boolean analog;





    private arduino_Poll arduino_poll;




    private arduino_Interrupt arduino_interrupt;


    public arduino_Sensor(
        boolean pullup,        boolean analog    ) {
        super(
        );
        this.pullup = pullup;
        this.analog = analog;
    }


    public boolean getPullup() {
        return pullup;
    }

    public void setPullup(boolean pullup) {
        this.pullup = pullup;
    }
    public boolean getAnalog() {
        return analog;
    }

    public void setAnalog(boolean analog) {
        this.analog = analog;
    }

    public arduino_Poll getArduino_poll() {
        return arduino_poll;
    }

    public void setArduino_poll(arduino_Poll arduino_poll) {
        this.arduino_poll = arduino_poll;
    }
    public arduino_Interrupt getArduino_interrupt() {
        return arduino_interrupt;
    }

    public void setArduino_interrupt(arduino_Interrupt arduino_interrupt) {
        this.arduino_interrupt = arduino_interrupt;
    }

}