





import java.util.List;
import java.util.ArrayList;

public class arduino_BooleanVariable extends Variable {

    private String value;
    private boolean initialValue;





    private arduino_BooleanVariableRef arduino_booleanvariableref;


    public arduino_BooleanVariable(
        String value,        boolean initialValue    ) {
        super(
        );
        this.value = value;
        this.initialValue = initialValue;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public boolean getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(boolean initialValue) {
        this.initialValue = initialValue;
    }

    public arduino_BooleanVariableRef getArduino_booleanvariableref() {
        return arduino_booleanvariableref;
    }

    public void setArduino_booleanvariableref(arduino_BooleanVariableRef arduino_booleanvariableref) {
        this.arduino_booleanvariableref = arduino_booleanvariableref;
    }

}