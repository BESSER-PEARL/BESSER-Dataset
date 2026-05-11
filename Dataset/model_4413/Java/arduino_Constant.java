





import java.util.List;
import java.util.ArrayList;

public class arduino_Constant extends Expression {

    private int value;





    private arduino_WaitFor arduino_waitfor;


    public arduino_Constant(
        int value    ) {
        super(
        );
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public arduino_WaitFor getArduino_waitfor() {
        return arduino_waitfor;
    }

    public void setArduino_waitfor(arduino_WaitFor arduino_waitfor) {
        this.arduino_waitfor = arduino_waitfor;
    }

}