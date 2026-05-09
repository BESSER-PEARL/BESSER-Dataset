





import java.util.List;
import java.util.ArrayList;

public class oaam_library_TaskType extends common_OaamBaseElementA, library_ResourceConsumerA {

    private boolean isDeterministic;
    private float preferredExecutionRate;



    public oaam_library_TaskType(
        boolean isDeterministic,        float preferredExecutionRate    ) {
        super(
        );
        this.isDeterministic = isDeterministic;
        this.preferredExecutionRate = preferredExecutionRate;
    }


    public boolean getIsdeterministic() {
        return isDeterministic;
    }

    public void setIsdeterministic(boolean isDeterministic) {
        this.isDeterministic = isDeterministic;
    }
    public float getPreferredexecutionrate() {
        return preferredExecutionRate;
    }

    public void setPreferredexecutionrate(float preferredExecutionRate) {
        this.preferredExecutionRate = preferredExecutionRate;
    }


}