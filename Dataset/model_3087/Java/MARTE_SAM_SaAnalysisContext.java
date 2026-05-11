





import java.util.List;
import java.util.ArrayList;

public class MARTE_SAM_SaAnalysisContext extends GaAnalysisContext {

    private String optCriterion;



    public MARTE_SAM_SaAnalysisContext(
        String optCriterion    ) {
        super(
        );
        this.optCriterion = optCriterion;
    }


    public String getOptcriterion() {
        return optCriterion;
    }

    public void setOptcriterion(String optCriterion) {
        this.optCriterion = optCriterion;
    }


}