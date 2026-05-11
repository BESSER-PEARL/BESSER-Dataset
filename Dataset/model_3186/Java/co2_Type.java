





import java.util.List;
import java.util.ArrayList;

public class co2_Type  {

    private String value;





    private co2_Variable co2_variable;




    private co2_Placeholder co2_placeholder;


    public co2_Type(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public co2_Variable getCo2_variable() {
        return co2_variable;
    }

    public void setCo2_variable(co2_Variable co2_variable) {
        this.co2_variable = co2_variable;
    }
    public co2_Placeholder getCo2_placeholder() {
        return co2_placeholder;
    }

    public void setCo2_placeholder(co2_Placeholder co2_placeholder) {
        this.co2_placeholder = co2_placeholder;
    }

}