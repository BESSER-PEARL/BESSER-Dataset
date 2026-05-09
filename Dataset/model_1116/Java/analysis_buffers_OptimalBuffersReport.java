





import java.util.List;
import java.util.ArrayList;

public class analysis_buffers_OptimalBuffersReport extends AnalysisReport {

    private boolean bitAccurate;
    private boolean pow2;



    public analysis_buffers_OptimalBuffersReport(
        boolean bitAccurate,        boolean pow2    ) {
        super(
        );
        this.bitAccurate = bitAccurate;
        this.pow2 = pow2;
    }


    public boolean getBitaccurate() {
        return bitAccurate;
    }

    public void setBitaccurate(boolean bitAccurate) {
        this.bitAccurate = bitAccurate;
    }
    public boolean getPow2() {
        return pow2;
    }

    public void setPow2(boolean pow2) {
        this.pow2 = pow2;
    }


}