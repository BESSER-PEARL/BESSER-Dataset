





import java.util.List;
import java.util.ArrayList;

public class UML2_Class extends EncapsulatedClassifier, BehavioredClassifier {

    private boolean isActive;





    private UML2_Class uml2_class;




    private UML2_Operation uml2_operation;




    private List<UML2_Operation> uml2_operations;


    public UML2_Class(
        boolean isActive    ) {
        super(
        );
        this.isActive = isActive;
        this.uml2_operations = new ArrayList<>();
    }

    public UML2_Class(
        boolean isActive        ArrayList<UML2_Operation> uml2_operations    ) {
        this.isActive = isActive;
        this.uml2_operations = uml2_operations;
    }

    public boolean getIsactive() {
        return isActive;
    }

    public void setIsactive(boolean isActive) {
        this.isActive = isActive;
    }

    public UML2_Class getUml2_class() {
        return uml2_class;
    }

    public void setUml2_class(UML2_Class uml2_class) {
        this.uml2_class = uml2_class;
    }
    public UML2_Operation getUml2_operation() {
        return uml2_operation;
    }

    public void setUml2_operation(UML2_Operation uml2_operation) {
        this.uml2_operation = uml2_operation;
    }
    public List<UML2_Operation> getUml2_operations() {
        return uml2_operations;
    }

    public void addUml2_operation(Uml2_operation uml2_operation) {
        this.uml2_operations.add(uml2_operation);
    }

}