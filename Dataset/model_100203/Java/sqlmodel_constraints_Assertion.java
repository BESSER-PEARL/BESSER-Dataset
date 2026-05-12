





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_constraints_Assertion extends Constraint {






    private List<BaseTable> basetables;




    private Schema schema;


    public sqlmodel_constraints_Assertion(
    ) {
        super(
        );
        this.basetables = new ArrayList<>();
    }

    public sqlmodel_constraints_Assertion(
        ArrayList<BaseTable> basetables    ) {
        this.basetables = basetables;
    }


    public List<BaseTable> getBasetables() {
        return basetables;
    }

    public void addBasetable(Basetable basetable) {
        this.basetables.add(basetable);
    }
    public Schema getSchema() {
        return schema;
    }

    public void setSchema(Schema schema) {
        this.schema = schema;
    }

}