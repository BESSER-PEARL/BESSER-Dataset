





import java.util.List;
import java.util.ArrayList;

public class vM_IntegerAttrDefComplement  {

    private String max;
    private String min;





    private vM_IntegerDeltaDef vm_integerdeltadef;




    private vM_IntegerAttrDefBounded vm_integerattrdefbounded;




    private vM_IntegerAttrDefBounded vm_integerattrdefbounded;


    public vM_IntegerAttrDefComplement(
        String max,        String min    ) {
        this.max = max;
        this.min = min;
    }


    public String getMax() {
        return max;
    }

    public void setMax(String max) {
        this.max = max;
    }
    public String getMin() {
        return min;
    }

    public void setMin(String min) {
        this.min = min;
    }

    public vM_IntegerDeltaDef getVm_integerdeltadef() {
        return vm_integerdeltadef;
    }

    public void setVm_integerdeltadef(vM_IntegerDeltaDef vm_integerdeltadef) {
        this.vm_integerdeltadef = vm_integerdeltadef;
    }
    public vM_IntegerAttrDefBounded getVm_integerattrdefbounded() {
        return vm_integerattrdefbounded;
    }

    public void setVm_integerattrdefbounded(vM_IntegerAttrDefBounded vm_integerattrdefbounded) {
        this.vm_integerattrdefbounded = vm_integerattrdefbounded;
    }
    public vM_IntegerAttrDefBounded getVm_integerattrdefbounded() {
        return vm_integerattrdefbounded;
    }

    public void setVm_integerattrdefbounded(vM_IntegerAttrDefBounded vm_integerattrdefbounded) {
        this.vm_integerattrdefbounded = vm_integerattrdefbounded;
    }

}