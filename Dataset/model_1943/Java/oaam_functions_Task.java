





import java.util.List;
import java.util.ArrayList;

public class oaam_functions_Task extends common_OaamBaseElementA, scenario_ModeDependentElementA, scenario_VariantDependentElementA {

    private float fixedRate;
    private int nParallels;



    public oaam_functions_Task(
        float fixedRate,        int nParallels    ) {
        super(
        );
        this.fixedRate = fixedRate;
        this.nParallels = nParallels;
    }


    public float getFixedrate() {
        return fixedRate;
    }

    public void setFixedrate(float fixedRate) {
        this.fixedRate = fixedRate;
    }
    public int getNparallels() {
        return nParallels;
    }

    public void setNparallels(int nParallels) {
        this.nParallels = nParallels;
    }


}