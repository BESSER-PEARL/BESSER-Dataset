





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_Relationship extends CloudMLElementWithProperties {






    private ProvidedPort providedport;




    private RequiredPort requiredport;


    public cloudml_core_Relationship(
    ) {
        super(
        );
    }



    public ProvidedPort getProvidedport() {
        return providedport;
    }

    public void setProvidedport(ProvidedPort providedport) {
        this.providedport = providedport;
    }
    public RequiredPort getRequiredport() {
        return requiredport;
    }

    public void setRequiredport(RequiredPort requiredport) {
        this.requiredport = requiredport;
    }

}