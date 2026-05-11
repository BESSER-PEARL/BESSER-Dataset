





import java.util.List;
import java.util.ArrayList;

public class vM_AttrDef  {

    private boolean runTime;
    private boolean notTranslatable;
    private boolean notDecidable;





    private vM_EnumAttrDef vm_enumattrdef;




    private vM_Attributes vm_attributes;




    private vM_BasicAttrDef vm_basicattrdef;


    public vM_AttrDef(
        boolean runTime,        boolean notTranslatable,        boolean notDecidable    ) {
        this.runTime = runTime;
        this.notTranslatable = notTranslatable;
        this.notDecidable = notDecidable;
    }


    public boolean getRuntime() {
        return runTime;
    }

    public void setRuntime(boolean runTime) {
        this.runTime = runTime;
    }
    public boolean getNottranslatable() {
        return notTranslatable;
    }

    public void setNottranslatable(boolean notTranslatable) {
        this.notTranslatable = notTranslatable;
    }
    public boolean getNotdecidable() {
        return notDecidable;
    }

    public void setNotdecidable(boolean notDecidable) {
        this.notDecidable = notDecidable;
    }

    public vM_EnumAttrDef getVm_enumattrdef() {
        return vm_enumattrdef;
    }

    public void setVm_enumattrdef(vM_EnumAttrDef vm_enumattrdef) {
        this.vm_enumattrdef = vm_enumattrdef;
    }
    public vM_Attributes getVm_attributes() {
        return vm_attributes;
    }

    public void setVm_attributes(vM_Attributes vm_attributes) {
        this.vm_attributes = vm_attributes;
    }
    public vM_BasicAttrDef getVm_basicattrdef() {
        return vm_basicattrdef;
    }

    public void setVm_basicattrdef(vM_BasicAttrDef vm_basicattrdef) {
        this.vm_basicattrdef = vm_basicattrdef;
    }

}