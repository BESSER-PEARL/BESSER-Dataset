





import java.util.List;
import java.util.ArrayList;

public class umlClass_AlternativeOperation extends Operation {






    private List<umlClass_Operation> umlclass_operations;


    public umlClass_AlternativeOperation(
    ) {
        super(
        );
        this.umlclass_operations = new ArrayList<>();
    }

    public umlClass_AlternativeOperation(
        ArrayList<umlClass_Operation> umlclass_operations    ) {
        this.umlclass_operations = umlclass_operations;
    }


    public List<umlClass_Operation> getUmlclass_operations() {
        return umlclass_operations;
    }

    public void addUmlclass_operation(Umlclass_operation umlclass_operation) {
        this.umlclass_operations.add(umlclass_operation);
    }

}