





import java.util.List;
import java.util.ArrayList;

public class UMLMM_Class extends EncapsulatedClassifier, BehavioredClassifier {






    private List<UMLMM_Operation> umlmm_operations;


    public UMLMM_Class(
    ) {
        super(
        );
        this.umlmm_operations = new ArrayList<>();
    }

    public UMLMM_Class(
        ArrayList<UMLMM_Operation> umlmm_operations    ) {
        this.umlmm_operations = umlmm_operations;
    }


    public List<UMLMM_Operation> getUmlmm_operations() {
        return umlmm_operations;
    }

    public void addUmlmm_operation(Umlmm_operation umlmm_operation) {
        this.umlmm_operations.add(umlmm_operation);
    }

}