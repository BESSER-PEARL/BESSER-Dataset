





import java.util.List;
import java.util.ArrayList;

public class jcl_parameters_AddressSpace extends parameters_Parameter, commons_ProcedureStepElement {

    private String value;



    public jcl_parameters_AddressSpace(
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