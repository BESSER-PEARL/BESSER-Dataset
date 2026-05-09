





import java.util.List;
import java.util.ArrayList;

public class oaam_capabilities_TaskOnDeviceCapability extends common_OaamBaseElementA, capabilities_CapabilityA, scenario_ModeDependentElementA, scenario_VariantDependentElementA {

    private float worstCaseExecutionTime;
    private float failureProbability;



    public oaam_capabilities_TaskOnDeviceCapability(
        float worstCaseExecutionTime,        float failureProbability    ) {
        super(
        );
        this.worstCaseExecutionTime = worstCaseExecutionTime;
        this.failureProbability = failureProbability;
    }


    public float getWorstcaseexecutiontime() {
        return worstCaseExecutionTime;
    }

    public void setWorstcaseexecutiontime(float worstCaseExecutionTime) {
        this.worstCaseExecutionTime = worstCaseExecutionTime;
    }
    public float getFailureprobability() {
        return failureProbability;
    }

    public void setFailureprobability(float failureProbability) {
        this.failureProbability = failureProbability;
    }


}