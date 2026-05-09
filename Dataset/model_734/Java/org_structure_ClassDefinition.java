





import java.util.List;
import java.util.ArrayList;

public class org_structure_ClassDefinition extends GenericTypeDefinition {

    private String isSingleton;
    private String isFinal;
    private String isAbstract;





    private List<structure_Operation> structure_operations;




    private List<structure_Constraint> structure_constraints;




    private List<structure_Property> structure_propertys;


    public org_structure_ClassDefinition(
        String isSingleton,        String isFinal,        String isAbstract    ) {
        super(
        );
        this.isSingleton = isSingleton;
        this.isFinal = isFinal;
        this.isAbstract = isAbstract;
        this.structure_operations = new ArrayList<>();
        this.structure_constraints = new ArrayList<>();
        this.structure_propertys = new ArrayList<>();
    }

    public org_structure_ClassDefinition(
        String isSingleton,        String isFinal,        String isAbstract        ArrayList<structure_Operation> structure_operations,        ArrayList<structure_Constraint> structure_constraints,        ArrayList<structure_Property> structure_propertys    ) {
        this.isSingleton = isSingleton;
        this.isFinal = isFinal;
        this.isAbstract = isAbstract;
        this.structure_operations = structure_operations;
        this.structure_constraints = structure_constraints;
        this.structure_propertys = structure_propertys;
    }

    public String getIssingleton() {
        return isSingleton;
    }

    public void setIssingleton(String isSingleton) {
        this.isSingleton = isSingleton;
    }
    public String getIsfinal() {
        return isFinal;
    }

    public void setIsfinal(String isFinal) {
        this.isFinal = isFinal;
    }
    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<structure_Operation> getStructure_operations() {
        return structure_operations;
    }

    public void addStructure_operation(Structure_operation structure_operation) {
        this.structure_operations.add(structure_operation);
    }
    public List<structure_Constraint> getStructure_constraints() {
        return structure_constraints;
    }

    public void addStructure_constraint(Structure_constraint structure_constraint) {
        this.structure_constraints.add(structure_constraint);
    }
    public List<structure_Property> getStructure_propertys() {
        return structure_propertys;
    }

    public void addStructure_property(Structure_property structure_property) {
        this.structure_propertys.add(structure_property);
    }

}