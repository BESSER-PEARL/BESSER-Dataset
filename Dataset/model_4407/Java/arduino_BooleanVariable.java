





import java.util.List;
import java.util.ArrayList;

public class arduino_BooleanVariable extends Variable {

    private boolean initialValue;





    private arduino_BooleanVariableRef arduino_booleanvariableref;


    public arduino_BooleanVariable(
        boolean initialValue    ) {
        super(
        );
        this.initialValue = initialValue;
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