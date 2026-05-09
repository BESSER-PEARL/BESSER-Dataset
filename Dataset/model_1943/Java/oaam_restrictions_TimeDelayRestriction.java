





import java.util.List;
import java.util.ArrayList;

public class oaam_restrictions_TimeDelayRestriction extends common_OaamBaseElementA, scenario_VariantDependentElementA, scenario_ModeDependentElementA {

    private float delay;



    public oaam_restrictions_TimeDelayRestriction(
        float delay    ) {
        super(
        );
        this.delay = delay;
    }


    public float getDelay() {
        return delay;
    }

    public void setDelay(float delay) {
        this.delay = delay;
    }


}