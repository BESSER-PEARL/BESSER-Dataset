





import java.util.List;
import java.util.ArrayList;

public class arduino_AbstractDevice  {

    private String name;
    private String pin;



    public arduino_AbstractDevice(
        String name,        String pin    ) {
        this.name = name;
        this.pin = pin;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPin() {
        return pin;
    }

    public void setPin(String pin) {
        this.pin = pin;
    }


}