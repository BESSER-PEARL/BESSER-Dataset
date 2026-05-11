





import java.util.List;
import java.util.ArrayList;

public class arduino_IntegerVariable extends Variable {

    private int initialValue;





    private arduino_IntegerVariableRef arduino_integervariableref;


    public arduino_IntegerVariable(
        int initialValue    ) {
        super(
        );
        this.initialValue = initialValue;
    }


    public int getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(int initialValue) {
        this.initialValue = initialValue;
    }

    public arduino_IntegerVariableRef getArduino_integervariableref() {
        return arduino_integervariableref;
    }

    public void setArduino_integervariableref(arduino_IntegerVariableRef arduino_integervariableref) {
        this.arduino_integervariableref = arduino_integervariableref;
    }

}