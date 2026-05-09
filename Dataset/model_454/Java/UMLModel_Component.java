





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Component extends Class {

    private String provided;
    private String indirectlyInstantiated;
    private String required;





    private List<UMLModel_PackageableElement> umlmodel_packageableelements;


    public UMLModel_Component(
        String provided,        String indirectlyInstantiated,        String required    ) {
        super(
        );
        this.provided = provided;
        this.indirectlyInstantiated = indirectlyInstantiated;
        this.required = required;
        this.umlmodel_packageableelements = new ArrayList<>();
    }

    public UMLModel_Component(
        String provided,        String indirectlyInstantiated,        String required        ArrayList<UMLModel_PackageableElement> umlmodel_packageableelements    ) {
        this.provided = provided;
        this.indirectlyInstantiated = indirectlyInstantiated;
        this.required = required;
        this.umlmodel_packageableelements = umlmodel_packageableelements;
    }

    public String getProvided() {
        return provided;
    }

    public void setProvided(String provided) {
        this.provided = provided;
    }
    public String getIndirectlyinstantiated() {
        return indirectlyInstantiated;
    }

    public void setIndirectlyinstantiated(String indirectlyInstantiated) {
        this.indirectlyInstantiated = indirectlyInstantiated;
    }
    public String getRequired() {
        return required;
    }

    public void setRequired(String required) {
        this.required = required;
    }

    public List<UMLModel_PackageableElement> getUmlmodel_packageableelements() {
        return umlmodel_packageableelements;
    }

    public void addUmlmodel_packageableelement(Umlmodel_packageableelement umlmodel_packageableelement) {
        this.umlmodel_packageableelements.add(umlmodel_packageableelement);
    }

}