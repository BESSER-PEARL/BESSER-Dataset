





import java.util.List;
import java.util.ArrayList;

public class vM_PairFeatureInteger  {

    private String value;





    private vM_Feature vm_feature;




    private vM_TableBasedValuationByAttributeForInteger vm_tablebasedvaluationbyattributeforinteger;


    public vM_PairFeatureInteger(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public vM_Feature getVm_feature() {
        return vm_feature;
    }

    public void setVm_feature(vM_Feature vm_feature) {
        this.vm_feature = vm_feature;
    }
    public vM_TableBasedValuationByAttributeForInteger getVm_tablebasedvaluationbyattributeforinteger() {
        return vm_tablebasedvaluationbyattributeforinteger;
    }

    public void setVm_tablebasedvaluationbyattributeforinteger(vM_TableBasedValuationByAttributeForInteger vm_tablebasedvaluationbyattributeforinteger) {
        this.vm_tablebasedvaluationbyattributeforinteger = vm_tablebasedvaluationbyattributeforinteger;
    }

}