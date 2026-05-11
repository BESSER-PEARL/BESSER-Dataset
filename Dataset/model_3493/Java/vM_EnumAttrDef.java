





import java.util.List;
import java.util.ArrayList;

public class vM_EnumAttrDef  {

    private String value;





    private vM_AttrDef vm_attrdef;


    public vM_EnumAttrDef(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public vM_AttrDef getVm_attrdef() {
        return vm_attrdef;
    }

    public void setVm_attrdef(vM_AttrDef vm_attrdef) {
        this.vm_attrdef = vm_attrdef;
    }

}