





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDAttributeGroupDefinition extends xsd_XSDRedefinableComponent, xsd_XSDAttributeGroupContent, xsd_XSDRedefineContent {

    private boolean attributeGroupDefinitionReference;



    public model_xsd_XSDAttributeGroupDefinition(
        boolean attributeGroupDefinitionReference    ) {
        super(
        );
        this.attributeGroupDefinitionReference = attributeGroupDefinitionReference;
    }


    public boolean getAttributegroupdefinitionreference() {
        return attributeGroupDefinitionReference;
    }

    public void setAttributegroupdefinitionreference(boolean attributeGroupDefinitionReference) {
        this.attributeGroupDefinitionReference = attributeGroupDefinitionReference;
    }


}