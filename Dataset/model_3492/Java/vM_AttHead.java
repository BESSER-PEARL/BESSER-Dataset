





import java.util.List;
import java.util.ArrayList;

public class vM_AttHead  {

    private boolean forAllFeatures;





    private vM_Abstract_ATT_ID vm_abstract_att_id;




    private vM_BasicAttrValuation vm_basicattrvaluation;




    private vM_PrimitiveExpression vm_primitiveexpression;




    private vM_Feature vm_feature;


    public vM_AttHead(
        boolean forAllFeatures    ) {
        this.forAllFeatures = forAllFeatures;
    }


    public boolean getForallfeatures() {
        return forAllFeatures;
    }

    public void setForallfeatures(boolean forAllFeatures) {
        this.forAllFeatures = forAllFeatures;
    }

    public vM_Abstract_ATT_ID getVm_abstract_att_id() {
        return vm_abstract_att_id;
    }

    public void setVm_abstract_att_id(vM_Abstract_ATT_ID vm_abstract_att_id) {
        this.vm_abstract_att_id = vm_abstract_att_id;
    }
    public vM_BasicAttrValuation getVm_basicattrvaluation() {
        return vm_basicattrvaluation;
    }

    public void setVm_basicattrvaluation(vM_BasicAttrValuation vm_basicattrvaluation) {
        this.vm_basicattrvaluation = vm_basicattrvaluation;
    }
    public vM_PrimitiveExpression getVm_primitiveexpression() {
        return vm_primitiveexpression;
    }

    public void setVm_primitiveexpression(vM_PrimitiveExpression vm_primitiveexpression) {
        this.vm_primitiveexpression = vm_primitiveexpression;
    }
    public vM_Feature getVm_feature() {
        return vm_feature;
    }

    public void setVm_feature(vM_Feature vm_feature) {
        this.vm_feature = vm_feature;
    }

}