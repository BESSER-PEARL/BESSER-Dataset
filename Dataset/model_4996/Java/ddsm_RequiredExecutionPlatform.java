





import java.util.List;
import java.util.ArrayList;

public class ddsm_RequiredExecutionPlatform extends ExecutionPlatform {

    private boolean isMandatory;





    private ddsm_ExecutionBinding ddsm_executionbinding;


    public ddsm_RequiredExecutionPlatform(
        boolean isMandatory    ) {
        super(
        );
        this.isMandatory = isMandatory;
    }


    public boolean getIsmandatory() {
        return isMandatory;
    }

    public void setIsmandatory(boolean isMandatory) {
        this.isMandatory = isMandatory;
    }

    public ddsm_ExecutionBinding getDdsm_executionbinding() {
        return ddsm_executionbinding;
    }

    public void setDdsm_executionbinding(ddsm_ExecutionBinding ddsm_executionbinding) {
        this.ddsm_executionbinding = ddsm_executionbinding;
    }

}