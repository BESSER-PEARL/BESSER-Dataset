





import java.util.List;
import java.util.ArrayList;

public class vM_BasicAttrValuation extends ExtendedValuation {

    private String value;





    private vM_Attributes vm_attributes;


    public vM_BasicAttrValuation(
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

    public vM_Attributes getVm_attributes() {
        return vm_attributes;
    }

    public void setVm_attributes(vM_Attributes vm_attributes) {
        this.vm_attributes = vm_attributes;
    }

}