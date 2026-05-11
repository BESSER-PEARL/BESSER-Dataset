





import java.util.List;
import java.util.ArrayList;

public class vM_Abstract_ATT_ID  {

    private String name;





    private vM_AttributeDescription vm_attributedescription;


    public vM_Abstract_ATT_ID(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public vM_AttributeDescription getVm_attributedescription() {
        return vm_attributedescription;
    }

    public void setVm_attributedescription(vM_AttributeDescription vm_attributedescription) {
        this.vm_attributedescription = vm_attributedescription;
    }

}