





import java.util.List;
import java.util.ArrayList;

public class analysis_buffers_BoundedBuffersReport extends AnalysisReport {

    private int tokenSize;
    private boolean pow2;
    private int bitSize;
    private boolean bitAccurate;



    public analysis_buffers_BoundedBuffersReport(
        int tokenSize,        boolean pow2,        int bitSize,        boolean bitAccurate    ) {
        super(
        );
        this.tokenSize = tokenSize;
        this.pow2 = pow2;
        this.bitSize = bitSize;
        this.bitAccurate = bitAccurate;
    }


    public int getTokensize() {
        return tokenSize;
    }

    public void setTokensize(int tokenSize) {
        this.tokenSize = tokenSize;
    }
    public boolean getPow2() {
        return pow2;
    }

    public void setPow2(boolean pow2) {
        this.pow2 = pow2;
    }
    public int getBitsize() {
        return bitSize;
    }

    public void setBitsize(int bitSize) {
        this.bitSize = bitSize;
    }
    public boolean getBitaccurate() {
        return bitAccurate;
    }

    public void setBitaccurate(boolean bitAccurate) {
        this.bitAccurate = bitAccurate;
    }


}