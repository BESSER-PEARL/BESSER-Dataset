





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_OperationGroup  {

    private String name;





    private List<operations_AbstractOperation> operations_abstractoperations;


    public esmodel_operations_OperationGroup(
        String name    ) {
        this.name = name;
        this.operations_abstractoperations = new ArrayList<>();
    }

    public esmodel_operations_OperationGroup(
        String name        ArrayList<operations_AbstractOperation> operations_abstractoperations    ) {
        this.name = name;
        this.operations_abstractoperations = operations_abstractoperations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<operations_AbstractOperation> getOperations_abstractoperations() {
        return operations_abstractoperations;
    }

    public void addOperations_abstractoperation(Operations_abstractoperation operations_abstractoperation) {
        this.operations_abstractoperations.add(operations_abstractoperation);
    }

}