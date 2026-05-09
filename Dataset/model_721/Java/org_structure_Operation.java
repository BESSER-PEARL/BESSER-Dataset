





import java.util.List;
import java.util.ArrayList;

public class org_structure_Operation extends structure_MultiplicityElement, structure_AbstractOperation {

    private String uniqueName;
    private String isAbstract;





    private List<structure_Constraint> structure_constraints;




    private List<structure_Parameter> structure_parameters;




    private behavior_Expression behavior_expression;




    private structure_ClassDefinition structure_classdefinition;




    private List<structure_Type> structure_types;




    private List<structure_Constraint> structure_constraints;




    private List<structure_UnresolvedOperation> structure_unresolvedoperations;


    public org_structure_Operation(
        String uniqueName,        String isAbstract    ) {
        super(
        );
        this.uniqueName = uniqueName;
        this.isAbstract = isAbstract;
        this.structure_constraints = new ArrayList<>();
        this.structure_parameters = new ArrayList<>();
        this.structure_types = new ArrayList<>();
        this.structure_constraints = new ArrayList<>();
        this.structure_unresolvedoperations = new ArrayList<>();
    }

    public org_structure_Operation(
        String uniqueName,        String isAbstract        ArrayList<structure_Constraint> structure_constraints,        ArrayList<structure_Parameter> structure_parameters,        ArrayList<structure_Type> structure_types,        ArrayList<structure_Constraint> structure_constraints,        ArrayList<structure_UnresolvedOperation> structure_unresolvedoperations    ) {
        this.uniqueName = uniqueName;
        this.isAbstract = isAbstract;
        this.structure_constraints = structure_constraints;
        this.structure_parameters = structure_parameters;
        this.structure_types = structure_types;
        this.structure_constraints = structure_constraints;
        this.structure_unresolvedoperations = structure_unresolvedoperations;
    }

    public String getUniquename() {
        return uniqueName;
    }

    public void setUniquename(String uniqueName) {
        this.uniqueName = uniqueName;
    }
    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<structure_Constraint> getStructure_constraints() {
        return structure_constraints;
    }

    public void addStructure_constraint(Structure_constraint structure_constraint) {
        this.structure_constraints.add(structure_constraint);
    }
    public List<structure_Parameter> getStructure_parameters() {
        return structure_parameters;
    }

    public void addStructure_parameter(Structure_parameter structure_parameter) {
        this.structure_parameters.add(structure_parameter);
    }
    public behavior_Expression getBehavior_expression() {
        return behavior_expression;
    }

    public void setBehavior_expression(behavior_Expression behavior_expression) {
        this.behavior_expression = behavior_expression;
    }
    public structure_ClassDefinition getStructure_classdefinition() {
        return structure_classdefinition;
    }

    public void setStructure_classdefinition(structure_ClassDefinition structure_classdefinition) {
        this.structure_classdefinition = structure_classdefinition;
    }
    public List<structure_Type> getStructure_types() {
        return structure_types;
    }

    public void addStructure_type(Structure_type structure_type) {
        this.structure_types.add(structure_type);
    }
    public List<structure_Constraint> getStructure_constraints() {
        return structure_constraints;
    }

    public void addStructure_constraint(Structure_constraint structure_constraint) {
        this.structure_constraints.add(structure_constraint);
    }
    public List<structure_UnresolvedOperation> getStructure_unresolvedoperations() {
        return structure_unresolvedoperations;
    }

    public void addStructure_unresolvedoperation(Structure_unresolvedoperation structure_unresolvedoperation) {
        this.structure_unresolvedoperations.add(structure_unresolvedoperation);
    }

}