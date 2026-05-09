





import java.util.List;
import java.util.ArrayList;

public class oaam_functions_FailureCondition extends common_OaamBaseElementA, scenario_VariantDependentElementA, scenario_ModeDependentElementA {

    private boolean noSingleFailure;
    private float maxOccurrenceProbability;



    public oaam_functions_FailureCondition(
        boolean noSingleFailure,        float maxOccurrenceProbability    ) {
        super(
        );
        this.noSingleFailure = noSingleFailure;
        this.maxOccurrenceProbability = maxOccurrenceProbability;
    }


    public boolean getNosinglefailure() {
        return noSingleFailure;
    }

    public void setNosinglefailure(boolean noSingleFailure) {
        this.noSingleFailure = noSingleFailure;
    }
    public float getMaxoccurrenceprobability() {
        return maxOccurrenceProbability;
    }

    public void setMaxoccurrenceprobability(float maxOccurrenceProbability) {
        this.maxOccurrenceProbability = maxOccurrenceProbability;
    }


}