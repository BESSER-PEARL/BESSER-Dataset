





import java.util.List;
import java.util.ArrayList;

public class model_testspecification_TestStep extends base_IContentElement, base_IPositionable {

    private String expectedOutcome;



    public model_testspecification_TestStep(
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