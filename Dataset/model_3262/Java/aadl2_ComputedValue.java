





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComputedValue extends PropertyValue {

    private String function;



    public aadl2_ComputedValue(
        String function    ) {
        super(
        );
        this.function = function;
    }


    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }


}