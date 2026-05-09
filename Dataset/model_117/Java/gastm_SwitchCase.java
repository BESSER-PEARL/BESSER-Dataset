





import java.util.List;
import java.util.ArrayList;

public class gastm_SwitchCase extends MinorSyntaxObject {

    private String isEvaluateAllCases;



    public gastm_SwitchCase(
        String isEvaluateAllCases    ) {
        super(
        );
        this.isEvaluateAllCases = isEvaluateAllCases;
    }


    public String getIsevaluateallcases() {
        return isEvaluateAllCases;
    }

    public void setIsevaluateallcases(String isEvaluateAllCases) {
        this.isEvaluateAllCases = isEvaluateAllCases;
    }


}