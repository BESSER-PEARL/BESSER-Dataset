





import java.util.List;
import java.util.ArrayList;

public class executionTrace_InstanceLinkModification extends Execution {

    private String targetInstanceObject;
    private String sourceInstanceObject;



    public executionTrace_InstanceLinkModification(
        String targetInstanceObject,        String sourceInstanceObject    ) {
        super(
        );
        this.targetInstanceObject = targetInstanceObject;
        this.sourceInstanceObject = sourceInstanceObject;
    }


    public String getTargetinstanceobject() {
        return targetInstanceObject;
    }

    public void setTargetinstanceobject(String targetInstanceObject) {
        this.targetInstanceObject = targetInstanceObject;
    }
    public String getSourceinstanceobject() {
        return sourceInstanceObject;
    }

    public void setSourceinstanceobject(String sourceInstanceObject) {
        this.sourceInstanceObject = sourceInstanceObject;
    }


}