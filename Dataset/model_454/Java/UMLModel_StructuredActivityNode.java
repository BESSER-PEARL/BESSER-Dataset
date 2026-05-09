





import java.util.List;
import java.util.ArrayList;

public class UMLModel_StructuredActivityNode extends ActivityGroup, Namespace, Action {

    private String mustIsolate;





    private List<UMLModel_Variable> umlmodel_variables;


    public UMLModel_StructuredActivityNode(
        String mustIsolate    ) {
        super(
        );
        this.mustIsolate = mustIsolate;
        this.umlmodel_variables = new ArrayList<>();
    }

    public UMLModel_StructuredActivityNode(
        String mustIsolate        ArrayList<UMLModel_Variable> umlmodel_variables    ) {
        this.mustIsolate = mustIsolate;
        this.umlmodel_variables = umlmodel_variables;
    }

    public String getMustisolate() {
        return mustIsolate;
    }

    public void setMustisolate(String mustIsolate) {
        this.mustIsolate = mustIsolate;
    }

    public List<UMLModel_Variable> getUmlmodel_variables() {
        return umlmodel_variables;
    }

    public void addUmlmodel_variable(Umlmodel_variable umlmodel_variable) {
        this.umlmodel_variables.add(umlmodel_variable);
    }

}