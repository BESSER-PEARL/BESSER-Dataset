





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDIdentityConstraintDefinition extends XSDNamedComponent {

    private String identityConstraintCategory;





    private XSDAnnotation xsdannotation;




    private XSDIdentityConstraintDefinition xsdidentityconstraintdefinition;


    public model_xsd_XSDIdentityConstraintDefinition(
        String identityConstraintCategory    ) {
        super(
        );
        this.identityConstraintCategory = identityConstraintCategory;
    }


    public String getIdentityconstraintcategory() {
        return identityConstraintCategory;
    }

    public void setIdentityconstraintcategory(String identityConstraintCategory) {
        this.identityConstraintCategory = identityConstraintCategory;
    }

    public XSDAnnotation getXsdannotation() {
        return xsdannotation;
    }

    public void setXsdannotation(XSDAnnotation xsdannotation) {
        this.xsdannotation = xsdannotation;
    }
    public XSDIdentityConstraintDefinition getXsdidentityconstraintdefinition() {
        return xsdidentityconstraintdefinition;
    }

    public void setXsdidentityconstraintdefinition(XSDIdentityConstraintDefinition xsdidentityconstraintdefinition) {
        this.xsdidentityconstraintdefinition = xsdidentityconstraintdefinition;
    }

}