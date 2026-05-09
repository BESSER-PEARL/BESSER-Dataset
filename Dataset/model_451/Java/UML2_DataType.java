





import java.util.List;
import java.util.ArrayList;

public class UML2_DataType extends Classifier {






    private List<UML2_Operation> uml2_operations;




    private UML2_Operation uml2_operation;


    public UML2_DataType(
    ) {
        super(
        );
        this.uml2_operations = new ArrayList<>();
    }

    public UML2_DataType(
        ArrayList<UML2_Operation> uml2_operations    ) {
        this.uml2_operations = uml2_operations;
    }


    public List<UML2_Operation> getUml2_operations() {
        return uml2_operations;
    }

    public void addUml2_operation(Uml2_operation uml2_operation) {
        this.uml2_operations.add(uml2_operation);
    }
    public UML2_Operation getUml2_operation() {
        return uml2_operation;
    }

    public void setUml2_operation(UML2_Operation uml2_operation) {
        this.uml2_operation = uml2_operation;
    }

}