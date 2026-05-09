





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ExecutionOccurrenceSpecification extends OccurrenceSpecification {

    private String execution;



    public UMLModel_ExecutionOccurrenceSpecification(
        String execution    ) {
        super(
        );
        this.execution = execution;
    }


    public String getExecution() {
        return execution;
    }

    public void setExecution(String execution) {
        this.execution = execution;
    }


}