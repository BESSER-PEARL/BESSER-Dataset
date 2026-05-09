





import java.util.List;
import java.util.ArrayList;

public class UMLModel_PackageImport extends DirectedRelationship {

    private String importingNamespace;
    private String visibility;





    private UMLModel_PackageableElement umlmodel_packageableelement;


    public UMLModel_PackageImport(
        String importingNamespace,        String visibility    ) {
        super(
        );
        this.importingNamespace = importingNamespace;
        this.visibility = visibility;
    }


    public String getImportingnamespace() {
        return importingNamespace;
    }

    public void setImportingnamespace(String importingNamespace) {
        this.importingNamespace = importingNamespace;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public UMLModel_PackageableElement getUmlmodel_packageableelement() {
        return umlmodel_packageableelement;
    }

    public void setUmlmodel_packageableelement(UMLModel_PackageableElement umlmodel_packageableelement) {
        this.umlmodel_packageableelement = umlmodel_packageableelement;
    }

}