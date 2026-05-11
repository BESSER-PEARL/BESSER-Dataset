





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_IntegerVariable extends IntegerExpression, Variable {

    private boolean currentValue;
    private int initialValue;



    public activitydiagram_IntegerVariable(
        boolean currentValue,        int initialValue    ) {
        super(
        );
        this.currentValue = currentValue;
        this.initialValue = initialValue;
    }


    public boolean getCurrentvalue() {
        return currentValue;
    }

    public void setCurrentvalue(boolean currentValue) {
        this.currentValue = currentValue;
    }
    public int getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(int initialValue) {
        this.initialValue = initialValue;
    }


}