





import java.util.List;
import java.util.ArrayList;

public class metamodel_Column  {

    private String name;
    private boolean nullable;
    private String size;
    private String type;





    private metamodel_Constraint metamodel_constraint;




    private List<metamodel_Constraint> metamodel_constraints;


    public metamodel_Column(
        String name,        boolean nullable,        String size,        String type    ) {
        this.name = name;
        this.nullable = nullable;
        this.size = size;
        this.type = type;
        this.metamodel_constraints = new ArrayList<>();
    }

    public metamodel_Column(
        String name,        boolean nullable,        String size,        String type        ArrayList<metamodel_Constraint> metamodel_constraints    ) {
        this.name = name;
        this.nullable = nullable;
        this.size = size;
        this.type = type;
        this.metamodel_constraints = metamodel_constraints;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public metamodel_Constraint getMetamodel_constraint() {
        return metamodel_constraint;
    }

    public void setMetamodel_constraint(metamodel_Constraint metamodel_constraint) {
        this.metamodel_constraint = metamodel_constraint;
    }
    public List<metamodel_Constraint> getMetamodel_constraints() {
        return metamodel_constraints;
    }

    public void addMetamodel_constraint(Metamodel_constraint metamodel_constraint) {
        this.metamodel_constraints.add(metamodel_constraint);
    }

}