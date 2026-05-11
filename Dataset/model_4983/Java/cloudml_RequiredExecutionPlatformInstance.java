





import java.util.List;
import java.util.ArrayList;

public class cloudml_RequiredExecutionPlatformInstance extends ExecutionPlatformInstance {






    private cloudml_InternalComponentInstance cloudml_internalcomponentinstance;




    private cloudml_ExecuteInstance cloudml_executeinstance;


    public cloudml_RequiredExecutionPlatformInstance(
    ) {
        super(
        );
    }



    public cloudml_InternalComponentInstance getCloudml_internalcomponentinstance() {
        return cloudml_internalcomponentinstance;
    }

    public void setCloudml_internalcomponentinstance(cloudml_InternalComponentInstance cloudml_internalcomponentinstance) {
        this.cloudml_internalcomponentinstance = cloudml_internalcomponentinstance;
    }
    public cloudml_ExecuteInstance getCloudml_executeinstance() {
        return cloudml_executeinstance;
    }

    public void setCloudml_executeinstance(cloudml_ExecuteInstance cloudml_executeinstance) {
        this.cloudml_executeinstance = cloudml_executeinstance;
    }

}