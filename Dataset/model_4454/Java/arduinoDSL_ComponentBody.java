





import java.util.List;
import java.util.ArrayList;

public class arduinoDSL_ComponentBody  {

    private String io;
    private int pin;
    private String type;





    private arduinoDSL_Component arduinodsl_component;


    public arduinoDSL_ComponentBody(
        String io,        int pin,        String type    ) {
        this.io = io;
        this.pin = pin;
        this.type = type;
    }


    public String getIo() {
        return io;
    }

    public void setIo(String io) {
        this.io = io;
    }
    public int getPin() {
        return pin;
    }

    public void setPin(int pin) {
        this.pin = pin;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public arduinoDSL_Component getArduinodsl_component() {
        return arduinodsl_component;
    }

    public void setArduinodsl_component(arduinoDSL_Component arduinodsl_component) {
        this.arduinodsl_component = arduinodsl_component;
    }

}