





import java.util.List;
import java.util.ArrayList;

public class analysis_partitioning_ComCostPartitioningReport extends AnalysisReport {

    private boolean bitAccurate;



    public analysis_partitioning_ComCostPartitioningReport(
        boolean bitAccurate    ) {
        super(
        );
        this.bitAccurate = bitAccurate;
    }


    public boolean getBitaccurate() {
        return bitAccurate;
    }

    public void setBitaccurate(boolean bitAccurate) {
        this.bitAccurate = bitAccurate;
    }


}