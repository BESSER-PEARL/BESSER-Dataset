





import java.util.List;
import java.util.ArrayList;

public class org_structure_Operation extends structure_MultiplicityElement, structure_AbstractOperation {

    private String uniqueName;
    private String isAbstract;





    private List<structure_Type> structure_types;




    private behavior_Expression behavior_expression;


    public org_structure_Operation(
        String uniqueName,        String isAbstract    ) {
        super(
        );
        this.uniqueName = uniqueName;
        this.isAbstract = isAbstract;
        this.structure_types = new ArrayList<>();
    }

    public org_structure_Operation(
        String uniqueName,        String isAbstract        ArrayList<structure_Type> structure_types    ) {
        this.uniqueName = uniqueName;
        this.isAbstract = isAbstract;
        this.structure_types = structure_types;
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

    public List<structure_Type> getStructure_types() {
        return structure_types;
    }

    public void addStructure_type(Structure_type structure_type) {
        this.structure_types.add(structure_type);
    }
    public behavior_Expression getBehavior_expression() {
        return behavior_expression;
    }

    public void setBehavior_expression(behavior_Expression behavior_expression) {
        this.behavior_expression = behavior_expression;
    }

}