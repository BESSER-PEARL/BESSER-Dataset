





import java.util.List;
import java.util.ArrayList;

public class automata_BooleanVariable extends Variable {

    private boolean initialValue;
    private boolean value;



    public automata_BooleanVariable(
        boolean initialValue,        boolean value    ) {
        super(
        );
        this.initialValue = initialValue;
        this.value = value;
    }


    public boolean getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(boolean initialValue) {
        this.initialValue = initialValue;
    }
    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }


}