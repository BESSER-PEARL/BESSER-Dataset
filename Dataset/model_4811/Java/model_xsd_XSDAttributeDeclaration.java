





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDAttributeDeclaration extends xsd_XSDSchemaContent, xsd_XSDFeature {

    private boolean attributeDeclarationReference;



    public model_xsd_XSDAttributeDeclaration(
        boolean attributeDeclarationReference    ) {
        super(
        );
        this.attributeDeclarationReference = attributeDeclarationReference;
    }


    public boolean getAttributedeclarationreference() {
        return attributeDeclarationReference;
    }

    public void setAttributedeclarationreference(boolean attributeDeclarationReference) {
        this.attributeDeclarationReference = attributeDeclarationReference;
    }


}