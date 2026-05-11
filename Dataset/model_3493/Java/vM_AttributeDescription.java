





import java.util.List;
import java.util.ArrayList;

public class vM_AttributeDescription  {

    private String description;





    private vM_Descriptions vm_descriptions;




    private vM_Feature vm_feature;


    public vM_AttributeDescription(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public vM_Descriptions getVm_descriptions() {
        return vm_descriptions;
    }

    public void setVm_descriptions(vM_Descriptions vm_descriptions) {
        this.vm_descriptions = vm_descriptions;
    }
    public vM_Feature getVm_feature() {
        return vm_feature;
    }

    public void setVm_feature(vM_Feature vm_feature) {
        this.vm_feature = vm_feature;
    }

}