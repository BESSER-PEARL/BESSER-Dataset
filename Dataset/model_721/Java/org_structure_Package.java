





import java.util.List;
import java.util.ArrayList;

public class org_structure_Package extends structure_ModelElementTypeDefinitionContainer, structure_NamedElement {

    private String uri;





    private structure_Package structure_package;




    private List<structure_Package> structure_packages;




    private List<structure_AdaptationOperator> structure_adaptationoperators;


    public org_structure_Package(
        String uri    ) {
        super(
        );
        this.uri = uri;
        this.structure_packages = new ArrayList<>();
        this.structure_adaptationoperators = new ArrayList<>();
    }

    public org_structure_Package(
        String uri        ArrayList<structure_Package> structure_packages,        ArrayList<structure_AdaptationOperator> structure_adaptationoperators    ) {
        this.uri = uri;
        this.structure_packages = structure_packages;
        this.structure_adaptationoperators = structure_adaptationoperators;
    }

    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }

    public structure_Package getStructure_package() {
        return structure_package;
    }

    public void setStructure_package(structure_Package structure_package) {
        this.structure_package = structure_package;
    }
    public List<structure_Package> getStructure_packages() {
        return structure_packages;
    }

    public void addStructure_package(Structure_package structure_package) {
        this.structure_packages.add(structure_package);
    }
    public List<structure_AdaptationOperator> getStructure_adaptationoperators() {
        return structure_adaptationoperators;
    }

    public void addStructure_adaptationoperator(Structure_adaptationoperator structure_adaptationoperator) {
        this.structure_adaptationoperators.add(structure_adaptationoperator);
    }

}