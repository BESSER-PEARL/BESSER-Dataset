





import java.util.List;
import java.util.ArrayList;

public class qm_FindingsMeasurementResult extends MeasurementResult {

    private String findings;
    private int count;



    public qm_FindingsMeasurementResult(
        String findings,        int count    ) {
        super(
        );
        this.findings = findings;
        this.count = count;
    }


    public String getFindings() {
        return findings;
    }

    public void setFindings(String findings) {
        this.findings = findings;
    }
    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }


}