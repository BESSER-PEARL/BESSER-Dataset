





import java.util.List;
import java.util.ArrayList;

public class uma_Milestone extends WorkBreakdownElement {

    private String requiredResult;



    public uma_Milestone(
        String requiredResult    ) {
        super(
        );
        this.requiredResult = requiredResult;
    }


    public String getRequiredresult() {
        return requiredResult;
    }

    public void setRequiredresult(String requiredResult) {
        this.requiredResult = requiredResult;
    }


}