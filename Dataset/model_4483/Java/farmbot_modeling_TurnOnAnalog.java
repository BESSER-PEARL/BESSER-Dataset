





import java.util.List;
import java.util.ArrayList;

public class farmbot_modeling_TurnOnAnalog extends SequenceCommand {

    private int pin;
    private int value;



    public farmbot_modeling_TurnOnAnalog(
        int pin,        int value    ) {
        super(
        );
        this.pin = pin;
        this.value = value;
    }


    public int getPin() {
        return pin;
    }

    public void setPin(int pin) {
        this.pin = pin;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}