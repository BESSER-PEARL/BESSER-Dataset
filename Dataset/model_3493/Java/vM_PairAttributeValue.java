





import java.util.List;
import java.util.ArrayList;

public class vM_PairAttributeValue  {

    private String value;





    private vM_TableBasedValuationByFeatureAndClone vm_tablebasedvaluationbyfeatureandclone;




    private vM_Abstract_ATT_ID vm_abstract_att_id;




    private vM_TableBasedValuationByFeature vm_tablebasedvaluationbyfeature;


    public vM_PairAttributeValue(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public vM_TableBasedValuationByFeatureAndClone getVm_tablebasedvaluationbyfeatureandclone() {
        return vm_tablebasedvaluationbyfeatureandclone;
    }

    public void setVm_tablebasedvaluationbyfeatureandclone(vM_TableBasedValuationByFeatureAndClone vm_tablebasedvaluationbyfeatureandclone) {
        this.vm_tablebasedvaluationbyfeatureandclone = vm_tablebasedvaluationbyfeatureandclone;
    }
    public vM_Abstract_ATT_ID getVm_abstract_att_id() {
        return vm_abstract_att_id;
    }

    public void setVm_abstract_att_id(vM_Abstract_ATT_ID vm_abstract_att_id) {
        this.vm_abstract_att_id = vm_abstract_att_id;
    }
    public vM_TableBasedValuationByFeature getVm_tablebasedvaluationbyfeature() {
        return vm_tablebasedvaluationbyfeature;
    }

    public void setVm_tablebasedvaluationbyfeature(vM_TableBasedValuationByFeature vm_tablebasedvaluationbyfeature) {
        this.vm_tablebasedvaluationbyfeature = vm_tablebasedvaluationbyfeature;
    }

}