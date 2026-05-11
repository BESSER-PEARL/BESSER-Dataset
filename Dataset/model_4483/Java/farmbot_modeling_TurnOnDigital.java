





import java.util.List;
import java.util.ArrayList;

public class farmbot_modeling_TurnOnDigital extends SequenceCommand {

    private int pin;



    public farmbot_modeling_TurnOnDigital(
        int pin    ) {
        super(
        );
        this.pin = pin;
    }


    public int getPin() {
        return pin;
    }

    public void setPin(int pin) {
        this.pin = pin;
    }


}