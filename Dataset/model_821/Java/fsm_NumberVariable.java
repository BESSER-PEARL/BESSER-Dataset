





import java.util.List;
import java.util.ArrayList;

public class fsm_NumberVariable extends Variable {

    private boolean value;
    private int initialValue;



    public fsm_NumberVariable(
        boolean value,        int initialValue    ) {
        super(
        );
        this.value = value;
        this.initialValue = initialValue;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }
    public int getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(int initialValue) {
        this.initialValue = initialValue;
    }


}