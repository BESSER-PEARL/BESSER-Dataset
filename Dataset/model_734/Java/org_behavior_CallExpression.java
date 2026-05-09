





import java.util.List;
import java.util.ArrayList;

public class org_behavior_CallExpression extends Expression {

    private String name;





    private List<structure_Type> structure_types;


    public org_behavior_CallExpression(
        String name    ) {
        super(
        );
        this.name = name;
        this.structure_types = new ArrayList<>();
    }

    public org_behavior_CallExpression(
        String name        ArrayList<structure_Type> structure_types    ) {
        this.name = name;
        this.structure_types = structure_types;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<structure_Type> getStructure_types() {
        return structure_types;
    }

    public void addStructure_type(Structure_type structure_type) {
        this.structure_types.add(structure_type);
    }

}