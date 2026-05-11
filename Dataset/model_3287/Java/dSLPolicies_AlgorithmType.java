





import java.util.List;
import java.util.ArrayList;

public class dSLPolicies_AlgorithmType  {

    private String type;





    private dSLPolicies_PathGeneratorStopCondition dslpolicies_pathgeneratorstopcondition;


    public dSLPolicies_AlgorithmType(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public dSLPolicies_PathGeneratorStopCondition getDslpolicies_pathgeneratorstopcondition() {
        return dslpolicies_pathgeneratorstopcondition;
    }

    public void setDslpolicies_pathgeneratorstopcondition(dSLPolicies_PathGeneratorStopCondition dslpolicies_pathgeneratorstopcondition) {
        this.dslpolicies_pathgeneratorstopcondition = dslpolicies_pathgeneratorstopcondition;
    }

}