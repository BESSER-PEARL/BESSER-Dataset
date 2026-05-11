





import java.util.List;
import java.util.ArrayList;

public class arduino_IntegerVariable extends Variable {

    private int initialValue;
    private String value;





    private arduino_IntegerVariableRef arduino_integervariableref;


    public arduino_IntegerVariable(
        int initialValue,        String value    ) {
        super(
        );
        this.initialValue = initialValue;
        this.value = value;
    }


    public int getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(int initialValue) {
        this.initialValue = initialValue;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public arduino_IntegerVariableRef getArduino_integervariableref() {
        return arduino_integervariableref;
    }

    public void setArduino_integervariableref(arduino_IntegerVariableRef arduino_integervariableref) {
        this.arduino_integervariableref = arduino_integervariableref;
    }

}