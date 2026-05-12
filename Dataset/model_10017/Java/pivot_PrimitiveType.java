





import java.util.List;
import java.util.ArrayList;

public class pivot_PrimitiveType extends DataType {






    private List<pivot_Operation> pivot_operations;


    public pivot_PrimitiveType(
    ) {
        super(
        );
        this.pivot_operations = new ArrayList<>();
    }

    public pivot_PrimitiveType(
        ArrayList<pivot_Operation> pivot_operations    ) {
        this.pivot_operations = pivot_operations;
    }


    public List<pivot_Operation> getPivot_operations() {
        return pivot_operations;
    }

    public void addPivot_operation(Pivot_operation pivot_operation) {
        this.pivot_operations.add(pivot_operation);
    }

}