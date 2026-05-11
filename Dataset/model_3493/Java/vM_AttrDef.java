





import java.util.List;
import java.util.ArrayList;

public class vM_AttrDef  {

    private boolean notDecidable;
    private boolean runTime;
    private boolean notTranslatable;





    private vM_Attributes vm_attributes;


    public vM_AttrDef(
        boolean notDecidable,        boolean runTime,        boolean notTranslatable    ) {
        this.notDecidable = notDecidable;
        this.runTime = runTime;
        this.notTranslatable = notTranslatable;
    }


    public boolean getNotdecidable() {
        return notDecidable;
    }

    public void setNotdecidable(boolean notDecidable) {
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

    public vM_Attributes getVm_attributes() {
        return vm_attributes;
    }

    public void setVm_attributes(vM_Attributes vm_attributes) {
        this.vm_attributes = vm_attributes;
    }

}