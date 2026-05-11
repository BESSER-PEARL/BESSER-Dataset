





import java.util.List;
import java.util.ArrayList;

public class vM_BooleanValuation  {

    private boolean notSelected;





    private vM_Feature vm_feature;




    private vM_Configuration vm_configuration;


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
    public vM_Configuration getVm_configuration() {
        return vm_configuration;
    }

    public void setVm_configuration(vM_Configuration vm_configuration) {
        this.vm_configuration = vm_configuration;
    }

}