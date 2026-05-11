





import java.util.List;
import java.util.ArrayList;

public class jcl_parameters_Other extends parameters_Parameter, commons_NamedElement, commons_ProcedureStepElement {

    private String value;



    public jcl_parameters_Other(
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