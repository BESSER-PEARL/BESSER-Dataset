





import java.util.List;
import java.util.ArrayList;

public class UMLModel_CallEvent extends MessageEvent {

    private String operation;



    public UMLModel_CallEvent(
        String operation    ) {
        super(
        );
        this.operation = operation;
    }


    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }


}