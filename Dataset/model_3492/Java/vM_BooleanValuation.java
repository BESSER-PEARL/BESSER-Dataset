





import java.util.List;
import java.util.ArrayList;

public class vM_BooleanValuation  {

    private boolean notSelected;





    private vM_Feature vm_feature;


    public vM_BooleanValuation(
        boolean notSelected    ) {
        this.notSelected = notSelected;
    }


    public boolean getNotselected() {
        return notSelected;
    }

    public void setNotselected(boolean notSelected) {
        this.notSelected = notSelected;
    }

    public vM_Feature getVm_feature() {
        return vm_feature;
    }

    public void setVm_feature(vM_Feature vm_feature) {
        this.vm_feature = vm_feature;
    }

}