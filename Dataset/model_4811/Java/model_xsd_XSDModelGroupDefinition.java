





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDModelGroupDefinition extends xsd_XSDRedefinableComponent, xsd_XSDRedefineContent, xsd_XSDParticleContent {

    private boolean modelGroupDefinitionReference;



    public model_xsd_XSDModelGroupDefinition(
        boolean modelGroupDefinitionReference    ) {
        super(
        );
        this.modelGroupDefinitionReference = modelGroupDefinitionReference;
    }


    public boolean getModelgroupdefinitionreference() {
        return modelGroupDefinitionReference;
    }

    public void setModelgroupdefinitionreference(boolean modelGroupDefinitionReference) {
        this.modelGroupDefinitionReference = modelGroupDefinitionReference;
    }


}