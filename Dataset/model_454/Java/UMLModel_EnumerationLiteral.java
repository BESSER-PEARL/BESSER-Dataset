





import java.util.List;
import java.util.ArrayList;

public class UMLModel_EnumerationLiteral extends InstanceSpecification {

    private String enumeration;





    private UMLModel_Enumeration umlmodel_enumeration;


    public UMLModel_EnumerationLiteral(
        String enumeration    ) {
        super(
        );
        this.enumeration = enumeration;
    }


    public String getEnumeration() {
        return enumeration;
    }

    public void setEnumeration(String enumeration) {
        this.enumeration = enumeration;
    }

    public UMLModel_Enumeration getUmlmodel_enumeration() {
        return umlmodel_enumeration;
    }

    public void setUmlmodel_enumeration(UMLModel_Enumeration umlmodel_enumeration) {
        this.umlmodel_enumeration = umlmodel_enumeration;
    }

}