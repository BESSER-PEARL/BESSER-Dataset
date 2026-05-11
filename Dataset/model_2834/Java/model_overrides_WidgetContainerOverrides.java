





import java.util.List;
import java.util.ArrayList;

public class model_overrides_WidgetContainerOverrides  {






    private List<Operation> operations;


    public model_overrides_WidgetContainerOverrides(
    ) {
        this.operations = new ArrayList<>();
    }

    public model_overrides_WidgetContainerOverrides(
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