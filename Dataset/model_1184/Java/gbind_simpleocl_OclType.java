





import java.util.List;
import java.util.ArrayList;

public class gbind_simpleocl_OclType extends LocatedElement {

    private String name;





    private Operation operation;


    public gbind_simpleocl_OclType(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Operation getOperation() {
        return operation;
    }

    public void setOperation(Operation operation) {
        this.operation = operation;
    }

}