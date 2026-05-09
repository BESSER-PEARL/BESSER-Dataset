





import java.util.List;
import java.util.ArrayList;

public class oaam_restrictions_SynchronicityRestriction extends common_OaamBaseElementA, restrictions_TaskRestrictionA, scenario_ModeDependentElementA, scenario_VariantDependentElementA {

    private float maxJitter;



    public oaam_restrictions_SynchronicityRestriction(
        float maxJitter    ) {
        super(
        );
        this.maxJitter = maxJitter;
    }


    public float getMaxjitter() {
        return maxJitter;
    }

    public void setMaxjitter(float maxJitter) {
        this.maxJitter = maxJitter;
    }


}