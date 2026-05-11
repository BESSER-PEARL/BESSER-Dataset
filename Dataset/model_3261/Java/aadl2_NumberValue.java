





import java.util.List;
import java.util.ArrayList;

public class aadl2_NumberValue extends PropertyValue {

    private String valueString;



    public aadl2_NumberValue(
        String valueString    ) {
        super(
        );
        this.valueString = valueString;
    }


    public String getValuestring() {
        return valueString;
    }

    public void setValuestring(String valueString) {
        this.valueString = valueString;
    }


}