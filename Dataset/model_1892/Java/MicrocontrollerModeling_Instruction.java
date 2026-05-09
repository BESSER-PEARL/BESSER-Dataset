





import java.util.List;
import java.util.ArrayList;

public class MicrocontrollerModeling_Instruction  {

    private String value;





    private MicrocontrollerModeling_Function microcontrollermodeling_function;


    public MicrocontrollerModeling_Instruction(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public MicrocontrollerModeling_Function getMicrocontrollermodeling_function() {
        return microcontrollermodeling_function;
    }

    public void setMicrocontrollermodeling_function(MicrocontrollerModeling_Function microcontrollermodeling_function) {
        this.microcontrollermodeling_function = microcontrollermodeling_function;
    }

}