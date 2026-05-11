





import java.util.List;
import java.util.ArrayList;

public class executionTrace_InstanceObjectModification extends Execution {

    private String instanceObject;



    public executionTrace_InstanceObjectModification(
        String instanceObject    ) {
        super(
        );
        this.instanceObject = instanceObject;
    }


    public String getInstanceobject() {
        return instanceObject;
    }

    public void setInstanceobject(String instanceObject) {
        this.instanceObject = instanceObject;
    }


}