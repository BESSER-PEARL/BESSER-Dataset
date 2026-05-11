





import java.util.List;
import java.util.ArrayList;

public class cloudml_ProvidedExecutionPlatformInstance extends ExecutionPlatformInstance {






    private cloudml_ComponentInstance cloudml_componentinstance;




    private cloudml_ExecuteInstance cloudml_executeinstance;


    public cloudml_ProvidedExecutionPlatformInstance(
    ) {
        super(
        );
    }



    public cloudml_ComponentInstance getCloudml_componentinstance() {
        return cloudml_componentinstance;
    }

    public void setCloudml_componentinstance(cloudml_ComponentInstance cloudml_componentinstance) {
        this.cloudml_componentinstance = cloudml_componentinstance;
    }
    public cloudml_ExecuteInstance getCloudml_executeinstance() {
        return cloudml_executeinstance;
    }

    public void setCloudml_executeinstance(cloudml_ExecuteInstance cloudml_executeinstance) {
        this.cloudml_executeinstance = cloudml_executeinstance;
    }

}