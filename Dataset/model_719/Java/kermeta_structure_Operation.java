





import java.util.List;
import java.util.ArrayList;

public class kermeta_structure_Operation extends MultiplicityElement {

    private String isAbstract;





    private behavior_Expression behavior_expression;




    private List<structure_Type> structure_types;




    private structure_Operation structure_operation;


    public kermeta_structure_Operation(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.structure_types = new ArrayList<>();
    }

    public kermeta_structure_Operation(
        String isAbstract        ArrayList<structure_Type> structure_types    ) {
        this.isAbstract = isAbstract;
        this.structure_types = structure_types;
    }

    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public behavior_Expression getBehavior_expression() {
        return behavior_expression;
    }

    public void setBehavior_expression(behavior_Expression behavior_expression) {
        this.behavior_expression = behavior_expression;
    }
    public List<structure_Type> getStructure_types() {
        return structure_types;
    }

    public void addStructure_type(Structure_type structure_type) {
        this.structure_types.add(structure_type);
    }
    public structure_Operation getStructure_operation() {
        return structure_operation;
    }

    public void setStructure_operation(structure_Operation structure_operation) {
        this.structure_operation = structure_operation;
    }

}