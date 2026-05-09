





import java.util.List;
import java.util.ArrayList;

public class rapidml_CollectionResource extends ServiceDataResource {

    private String resourceRealizationKind;



    public rapidml_CollectionResource(
        String resourceRealizationKind    ) {
        super(
        );
        this.resourceRealizationKind = resourceRealizationKind;
    }


    public String getResourcerealizationkind() {
        return resourceRealizationKind;
    }

    public void setResourcerealizationkind(String resourceRealizationKind) {
        this.resourceRealizationKind = resourceRealizationKind;
    }


}