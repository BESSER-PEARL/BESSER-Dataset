





import java.util.List;
import java.util.ArrayList;

public class vM_RealDefaultDef  {

    private String value;





    private vM_RealAttrDef vm_realattrdef;


    public vM_RealDefaultDef(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public vM_RealAttrDef getVm_realattrdef() {
        return vm_realattrdef;
    }

    public void setVm_realattrdef(vM_RealAttrDef vm_realattrdef) {
        this.vm_realattrdef = vm_realattrdef;
    }

}