





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_InstanceService extends Service {

    private String instanceName;



    public appBuilderDSL_InstanceService(
        String instanceName    ) {
        super(
        );
        this.instanceName = instanceName;
    }


    public String getInstancename() {
        return instanceName;
    }

    public void setInstancename(String instanceName) {
        this.instanceName = instanceName;
    }


}