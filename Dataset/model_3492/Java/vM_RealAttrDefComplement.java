





import java.util.List;
import java.util.ArrayList;

public class vM_RealAttrDefComplement  {

    private String max;
    private String min;





    private vM_RealAttrDefBounded vm_realattrdefbounded;


    public vM_RealAttrDefComplement(
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

    public vM_RealAttrDefBounded getVm_realattrdefbounded() {
        return vm_realattrdefbounded;
    }

    public void setVm_realattrdefbounded(vM_RealAttrDefBounded vm_realattrdefbounded) {
        this.vm_realattrdefbounded = vm_realattrdefbounded;
    }

}