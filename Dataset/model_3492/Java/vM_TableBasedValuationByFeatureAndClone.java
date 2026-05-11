





import java.util.List;
import java.util.ArrayList;

public class vM_TableBasedValuationByFeatureAndClone  {

    private String name;





    private vM_Feature vm_feature;




    private vM_AdvancedAttrValuation vm_advancedattrvaluation;


    public vM_TableBasedValuationByFeatureAndClone(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public vM_Feature getVm_feature() {
        return vm_feature;
    }

    public void setVm_feature(vM_Feature vm_feature) {
        this.vm_feature = vm_feature;
    }
    public vM_AdvancedAttrValuation getVm_advancedattrvaluation() {
        return vm_advancedattrvaluation;
    }

    public void setVm_advancedattrvaluation(vM_AdvancedAttrValuation vm_advancedattrvaluation) {
        this.vm_advancedattrvaluation = vm_advancedattrvaluation;
    }

}