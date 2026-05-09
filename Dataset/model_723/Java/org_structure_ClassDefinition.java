





import java.util.List;
import java.util.ArrayList;

public class org_structure_ClassDefinition extends GenericTypeDefinition {

    private String isAbstract;
    private String isFinal;
    private String isSingleton;





    private List<structure_Operation> structure_operations;




    private List<structure_Property> structure_propertys;




    private List<structure_Constraint> structure_constraints;


    public org_structure_ClassDefinition(
        String isAbstract,        String isFinal,        String isSingleton    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.isFinal = isFinal;
        this.isSingleton = isSingleton;
        this.structure_operations = new ArrayList<>();
        this.structure_propertys = new ArrayList<>();
        this.structure_constraints = new ArrayList<>();
    }

    public org_structure_ClassDefinition(
        String isAbstract,        String isFinal,        String isSingleton        ArrayList<structure_Operation> structure_operations,        ArrayList<structure_Property> structure_propertys,        ArrayList<structure_Constraint> structure_constraints    ) {
        this.isAbstract = isAbstract;
        this.isFinal = isFinal;
        this.isSingleton = isSingleton;
        this.structure_operations = structure_operations;
        this.structure_propertys = structure_propertys;
        this.structure_constraints = structure_constraints;
    }

    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }
    public String getIsfinal() {
        return isFinal;
    }

    public void setIsfinal(String isFinal) {
        this.isFinal = isFinal;
    }
    public String getIssingleton() {
        return isSingleton;
    }

    public void setIssingleton(String isSingleton) {
        this.isSingleton = isSingleton;
    }

    public List<structure_Operation> getStructure_operations() {
        return structure_operations;
    }

    public void addStructure_operation(Structure_operation structure_operation) {
        this.structure_operations.add(structure_operation);
    }
    public List<structure_Property> getStructure_propertys() {
        return structure_propertys;
    }

    public void addStructure_property(Structure_property structure_property) {
        this.structure_propertys.add(structure_property);
    }
    public List<structure_Constraint> getStructure_constraints() {
        return structure_constraints;
    }

    public void addStructure_constraint(Structure_constraint structure_constraint) {
        this.structure_constraints.add(structure_constraint);
    }

}