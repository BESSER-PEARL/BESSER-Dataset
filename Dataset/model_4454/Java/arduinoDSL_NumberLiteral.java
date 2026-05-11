





import java.util.List;
import java.util.ArrayList;

public class arduinoDSL_NumberLiteral extends Value {

    private String floatVal;
    private int intVal;



    public arduinoDSL_NumberLiteral(
        String floatVal,        int intVal    ) {
        super(
        );
        this.floatVal = floatVal;
        this.intVal = intVal;
    }


    public String getFloatval() {
        return floatVal;
    }

    public void setFloatval(String floatVal) {
        this.floatVal = floatVal;
    }
    public int getIntval() {
        return intVal;
    }

    public void setIntval(int intVal) {
        this.intVal = intVal;
    }


}