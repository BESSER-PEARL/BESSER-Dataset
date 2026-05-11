





import java.util.List;
import java.util.ArrayList;

public class qm_FindingsMeasurementResult extends MeasurementResult {

    private int count;
    private String findings;



    public qm_FindingsMeasurementResult(
        int count,        String findings    ) {
        super(
        );
        this.count = count;
        this.findings = findings;
    }


    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }
    public String getFindings() {
        return findings;
    }

    public void setFindings(String findings) {
        this.findings = findings;
    }


}