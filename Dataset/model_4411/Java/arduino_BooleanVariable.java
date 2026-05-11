





import java.util.List;
import java.util.ArrayList;

public class arduino_BooleanVariable extends BooleanExpression, Variable {

    private boolean initialValue;



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


}