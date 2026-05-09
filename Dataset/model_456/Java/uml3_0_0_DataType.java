





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_DataType extends Classifier {






    private List<uml3_0_0_Operation> uml3_0_0_operations;




    private uml3_0_0_Operation uml3_0_0_operation;


    public uml3_0_0_DataType(
    ) {
        super(
        );
        this.uml3_0_0_operations = new ArrayList<>();
    }

    public uml3_0_0_DataType(
        ArrayList<uml3_0_0_Operation> uml3_0_0_operations    ) {
        this.uml3_0_0_operations = uml3_0_0_operations;
    }


    public List<uml3_0_0_Operation> getUml3_0_0_operations() {
        return uml3_0_0_operations;
    }

    public void addUml3_0_0_operation(Uml3_0_0_operation uml3_0_0_operation) {
        this.uml3_0_0_operations.add(uml3_0_0_operation);
    }
    public uml3_0_0_Operation getUml3_0_0_operation() {
        return uml3_0_0_operation;
    }

    public void setUml3_0_0_operation(uml3_0_0_Operation uml3_0_0_operation) {
        this.uml3_0_0_operation = uml3_0_0_operation;
    }

}