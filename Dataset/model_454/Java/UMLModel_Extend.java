





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Extend extends NamedElement, DirectedRelationship {

    private String extensionLocation;
    private String extension;
    private String extendedCase;





    private UMLModel_Constraint umlmodel_constraint;


    public UMLModel_Extend(
        String extensionLocation,        String extension,        String extendedCase    ) {
        super(
        );
        this.extensionLocation = extensionLocation;
        this.extension = extension;
        this.extendedCase = extendedCase;
    }


    public String getExtensionlocation() {
        return extensionLocation;
    }

    public void setExtensionlocation(String extensionLocation) {
        this.extensionLocation = extensionLocation;
    }
    public String getExtension() {
        return extension;
    }

    public void setExtension(String extension) {
        this.extension = extension;
    }
    public String getExtendedcase() {
        return extendedCase;
    }

    public void setExtendedcase(String extendedCase) {
        this.extendedCase = extendedCase;
    }

    public UMLModel_Constraint getUmlmodel_constraint() {
        return umlmodel_constraint;
    }

    public void setUmlmodel_constraint(UMLModel_Constraint umlmodel_constraint) {
        this.umlmodel_constraint = umlmodel_constraint;
    }

}