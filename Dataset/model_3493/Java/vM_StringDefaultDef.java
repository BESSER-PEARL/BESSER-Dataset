





import java.util.List;
import java.util.ArrayList;

public class vM_StringDefaultDef  {

    private String value;





    private vM_StringAttrDef vm_stringattrdef;


    public vM_StringDefaultDef(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public vM_StringAttrDef getVm_stringattrdef() {
        return vm_stringattrdef;
    }

    public void setVm_stringattrdef(vM_StringAttrDef vm_stringattrdef) {
        this.vm_stringattrdef = vm_stringattrdef;
    }

}