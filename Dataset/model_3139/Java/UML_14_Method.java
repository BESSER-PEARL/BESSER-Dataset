





import java.util.List;
import java.util.ArrayList;

public class UML_14_Method extends BehavioralFeature {

    private String body;





    private List<UML_14_Operation> uml_14_operations;


    public UML_14_Method(
        String body    ) {
        super(
        );
        this.body = body;
        this.uml_14_operations = new ArrayList<>();
    }

    public UML_14_Method(
        String body        ArrayList<UML_14_Operation> uml_14_operations    ) {
        this.body = body;
        this.uml_14_operations = uml_14_operations;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public List<UML_14_Operation> getUml_14_operations() {
        return uml_14_operations;
    }

    public void addUml_14_operation(Uml_14_operation uml_14_operation) {
        this.uml_14_operations.add(uml_14_operation);
    }

}