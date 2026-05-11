





import java.util.List;
import java.util.ArrayList;

public class arduino_IntegerVariable extends IntegerExpression, Variable {

    private int initialValue;



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


}