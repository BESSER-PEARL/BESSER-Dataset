





import java.util.List;
import java.util.ArrayList;

public class rapidml_TypedMessage extends WithExamples, RealizationContainer, RESTElement {

    private boolean useParentTypeReference;





    private rapidml_ResourceDefinition rapidml_resourcedefinition;


    public rapidml_TypedMessage(
        boolean useParentTypeReference    ) {
        super(
        );
        this.useParentTypeReference = useParentTypeReference;
    }


    public boolean getUseparenttypereference() {
        return useParentTypeReference;
    }

    public void setUseparenttypereference(boolean useParentTypeReference) {
        this.useParentTypeReference = useParentTypeReference;
    }

    public rapidml_ResourceDefinition getRapidml_resourcedefinition() {
        return rapidml_resourcedefinition;
    }

    public void setRapidml_resourcedefinition(rapidml_ResourceDefinition rapidml_resourcedefinition) {
        this.rapidml_resourcedefinition = rapidml_resourcedefinition;
    }

}