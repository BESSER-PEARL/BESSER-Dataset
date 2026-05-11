





import java.util.List;
import java.util.ArrayList;

public class model_processes_ProcessStep extends ProcessNode {

    private String expectedOutcome;



    public model_processes_ProcessStep(
        String expectedOutcome    ) {
        super(
        );
        this.expectedOutcome = expectedOutcome;
    }


    public String getExpectedoutcome() {
        return expectedOutcome;
    }

    public void setExpectedoutcome(String expectedOutcome) {
        this.expectedOutcome = expectedOutcome;
    }


}