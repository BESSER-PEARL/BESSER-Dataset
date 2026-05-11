





import java.util.List;
import java.util.ArrayList;

public class smm_AggregatedMeasurement extends DimensionalMeasurement {

    private boolean isBaseSuppled;



    public smm_AggregatedMeasurement(
        boolean isBaseSuppled    ) {
        super(
        );
        this.isBaseSuppled = isBaseSuppled;
    }


    public boolean getIsbasesuppled() {
        return isBaseSuppled;
    }

    public void setIsbasesuppled(boolean isBaseSuppled) {
        this.isBaseSuppled = isBaseSuppled;
    }


}