





import java.util.List;
import java.util.ArrayList;

public class ardlers_ComponentBody  {

    private String io;
    private String type;
    private int pin;
    private String pinned;





    private ardlers_Component ardlers_component;


    public ardlers_ComponentBody(
        String io,        String type,        int pin,        String pinned    ) {
        this.io = io;
        this.type = type;
        this.pin = pin;
        this.pinned = pinned;
    }


    public String getIo() {
        return io;
    }

    public void setIo(String io) {
        this.io = io;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getPin() {
        return pin;
    }

    public void setPin(int pin) {
        this.pin = pin;
    }
    public String getPinned() {
        return pinned;
    }

    public void setPinned(String pinned) {
        this.pinned = pinned;
    }

    public ardlers_Component getArdlers_component() {
        return ardlers_component;
    }

    public void setArdlers_component(ardlers_Component ardlers_component) {
        this.ardlers_component = ardlers_component;
    }

}