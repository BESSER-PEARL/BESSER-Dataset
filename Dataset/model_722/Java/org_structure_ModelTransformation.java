





import java.util.List;
import java.util.ArrayList;

public class org_structure_ModelTransformation extends MultiplicityElement {

    private String isAbstract;





    private List<structure_Parameter> structure_parameters;




    private List<structure_Operation> structure_operations;




    private List<structure_ModelTypeVariable> structure_modeltypevariables;




    private structure_ModelTypeDefinition structure_modeltypedefinition;


    public org_structure_ModelTransformation(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.structure_parameters = new ArrayList<>();
        this.structure_operations = new ArrayList<>();
        this.structure_modeltypevariables = new ArrayList<>();
    }

    public org_structure_ModelTransformation(
        String isAbstract        ArrayList<structure_Parameter> structure_parameters,        ArrayList<structure_Operation> structure_operations,        ArrayList<structure_ModelTypeVariable> structure_modeltypevariables    ) {
        this.isAbstract = isAbstract;
        this.structure_parameters = structure_parameters;
        this.structure_operations = structure_operations;
        this.structure_modeltypevariables = structure_modeltypevariables;
    }

    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<structure_Parameter> getStructure_parameters() {
        return structure_parameters;
    }

    public void addStructure_parameter(Structure_parameter structure_parameter) {
        this.structure_parameters.add(structure_parameter);
    }
    public List<structure_Operation> getStructure_operations() {
        return structure_operations;
    }

    public void addStructure_operation(Structure_operation structure_operation) {
        this.structure_operations.add(structure_operation);
    }
    public List<structure_ModelTypeVariable> getStructure_modeltypevariables() {
        return structure_modeltypevariables;
    }

    public void addStructure_modeltypevariable(Structure_modeltypevariable structure_modeltypevariable) {
        this.structure_modeltypevariables.add(structure_modeltypevariable);
    }
    public structure_ModelTypeDefinition getStructure_modeltypedefinition() {
        return structure_modeltypedefinition;
    }

    public void setStructure_modeltypedefinition(structure_ModelTypeDefinition structure_modeltypedefinition) {
        this.structure_modeltypedefinition = structure_modeltypedefinition;
    }

}