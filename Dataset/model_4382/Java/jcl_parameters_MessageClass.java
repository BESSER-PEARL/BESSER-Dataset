





import java.util.List;
import java.util.ArrayList;

public class jcl_parameters_MessageClass extends Parameter {

    private String value;



    public jcl_parameters_MessageClass(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}