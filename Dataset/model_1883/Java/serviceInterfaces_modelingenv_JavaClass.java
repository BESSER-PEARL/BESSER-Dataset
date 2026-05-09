





import java.util.List;
import java.util.ArrayList;

public class serviceInterfaces_modelingenv_JavaClass extends JavaTypeDeclaration {






    private List<Operation> operations;


    public serviceInterfaces_modelingenv_JavaClass(
    ) {
        super(
        );
        this.operations = new ArrayList<>();
    }

    public serviceInterfaces_modelingenv_JavaClass(
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