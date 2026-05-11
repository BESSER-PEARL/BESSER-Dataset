





import java.util.List;
import java.util.ArrayList;

public class MARTE_SAM_SaAnalysisContext extends GaAnalysisContext {

    private String isSched;
    private String optCriterion;



    public MARTE_SAM_SaAnalysisContext(
        String isSched,        String optCriterion    ) {
        super(
        );
        this.isSched = isSched;
        this.optCriterion = optCriterion;
    }


    public String getIssched() {
        return isSched;
    }

    public void setIssched(String isSched) {
        this.isSched = isSched;
    }
    public String getOptcriterion() {
        return optCriterion;
    }

    public void setOptcriterion(String optCriterion) {
        this.optCriterion = optCriterion;
    }


}