





import java.util.List;
import java.util.ArrayList;

public class camel_requirement_QualitativeHardwareRequirement extends HardwareRequirement {

    private float minBenchmark;
    private float maxBenchmark;



    public camel_requirement_QualitativeHardwareRequirement(
        float minBenchmark,        float maxBenchmark    ) {
        super(
        );
        this.minBenchmark = minBenchmark;
        this.maxBenchmark = maxBenchmark;
    }


    public float getMinbenchmark() {
        return minBenchmark;
    }

    public void setMinbenchmark(float minBenchmark) {
        this.minBenchmark = minBenchmark;
    }
    public float getMaxbenchmark() {
        return maxBenchmark;
    }

    public void setMaxbenchmark(float maxBenchmark) {
        this.maxBenchmark = maxBenchmark;
    }


}