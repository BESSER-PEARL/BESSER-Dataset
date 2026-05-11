





import java.util.List;
import java.util.ArrayList;

public class model_wsdl_BindingOperation extends wsdl_IBindingOperation, wsdl_ExtensibleElement {

    private String name;





    private Operation operation;


    public model_wsdl_BindingOperation(
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