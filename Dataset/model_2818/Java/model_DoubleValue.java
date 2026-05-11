





import java.util.List;
import java.util.ArrayList;

public class model_DoubleValue extends Value {

    private int valueInt;
    private int valueDecimal;



    public model_DoubleValue(
        int valueInt,        int valueDecimal    ) {
        super(
        );
        this.valueInt = valueInt;
        this.valueDecimal = valueDecimal;
    }


    public int getValueint() {
        return valueInt;
    }

    public void setValueint(int valueInt) {
        this.valueInt = valueInt;
    }
    public int getValuedecimal() {
        return valueDecimal;
    }

    public void setValuedecimal(int valueDecimal) {
        this.valueDecimal = valueDecimal;
    }


}