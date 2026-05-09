





import java.util.List;
import java.util.ArrayList;

public class oaam_functions_Output extends common_OaamBaseElementA, scenario_ModeDependentElementA, scenario_VariantDependentElementA {

    private float fixedRate;



    public oaam_functions_Output(
        float fixedRate    ) {
        super(
        );
        this.fixedRate = fixedRate;
    }


    public float getFixedrate() {
        return fixedRate;
    }

    public void setFixedrate(float fixedRate) {
        this.fixedRate = fixedRate;
    }


}