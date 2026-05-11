





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_ExecuteInstance extends CloudMLElementWithProperties {






    private ProvidedExecutionPlatformInstance providedexecutionplatforminstance;




    private RequiredExecutionPlatformInstance requiredexecutionplatforminstance;


    public cloudml_core_ExecuteInstance(
    ) {
        super(
        );
    }



    public ProvidedExecutionPlatformInstance getProvidedexecutionplatforminstance() {
        return providedexecutionplatforminstance;
    }

    public void setProvidedexecutionplatforminstance(ProvidedExecutionPlatformInstance providedexecutionplatforminstance) {
        this.providedexecutionplatforminstance = providedexecutionplatforminstance;
    }
    public RequiredExecutionPlatformInstance getRequiredexecutionplatforminstance() {
        return requiredexecutionplatforminstance;
    }

    public void setRequiredexecutionplatforminstance(RequiredExecutionPlatformInstance requiredexecutionplatforminstance) {
        this.requiredexecutionplatforminstance = requiredexecutionplatforminstance;
    }

}