





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_ComponentInstance extends CloudMLElementWithProperties {






    private List<ProvidedExecutionPlatformInstance> providedexecutionplatforminstances;


    public cloudml_core_ComponentInstance(
    ) {
        super(
        );
        this.providedexecutionplatforminstances = new ArrayList<>();
    }

    public cloudml_core_ComponentInstance(
        ArrayList<ProvidedExecutionPlatformInstance> providedexecutionplatforminstances    ) {
        this.providedexecutionplatforminstances = providedexecutionplatforminstances;
    }


    public List<ProvidedExecutionPlatformInstance> getProvidedexecutionplatforminstances() {
        return providedexecutionplatforminstances;
    }

    public void addProvidedexecutionplatforminstance(Providedexecutionplatforminstance providedexecutionplatforminstance) {
        this.providedexecutionplatforminstances.add(providedexecutionplatforminstance);
    }

}