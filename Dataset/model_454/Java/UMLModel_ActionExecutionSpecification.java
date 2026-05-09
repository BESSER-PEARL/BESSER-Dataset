





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ActionExecutionSpecification extends ExecutionSpecification {

    private String action;



    public UMLModel_ActionExecutionSpecification(
        String action    ) {
        super(
        );
        this.action = action;
    }


    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }


}