





import java.util.List;
import java.util.ArrayList;

public class mm_rdb_ModelRoot  {






    private List<Operation> operations;


    public mm_rdb_ModelRoot(
    ) {
        this.operations = new ArrayList<>();
    }

    public mm_rdb_ModelRoot(
        ArrayList<Operation> operations    ) {
        this.operations = operations;
    }


    public List<Operation> getOperations() {
        return operations;
    }

    public void addOperation(Operation operation) {
        this.operations.add(operation);
    }

}