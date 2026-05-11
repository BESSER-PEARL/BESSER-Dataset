





import java.util.List;
import java.util.ArrayList;

public class vM_PairFeatureReal  {

    private String value;





    private vM_Feature vm_feature;




    private vM_TableBasedValuationByAttributeForReal vm_tablebasedvaluationbyattributeforreal;


    public vM_PairFeatureReal(
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
    public vM_TableBasedValuationByAttributeForReal getVm_tablebasedvaluationbyattributeforreal() {
        return vm_tablebasedvaluationbyattributeforreal;
    }

    public void setVm_tablebasedvaluationbyattributeforreal(vM_TableBasedValuationByAttributeForReal vm_tablebasedvaluationbyattributeforreal) {
        this.vm_tablebasedvaluationbyattributeforreal = vm_tablebasedvaluationbyattributeforreal;
    }

}