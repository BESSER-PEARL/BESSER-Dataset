





import java.util.List;
import java.util.ArrayList;

public class UATMM_structure_KofN extends Connector {

    private int Threshold;



    public UATMM_structure_KofN(
        int Threshold    ) {
        super(
        );
        this.Threshold = Threshold;
    }


    public int getThreshold() {
        return Threshold;
    }

    public void setThreshold(int Threshold) {
        this.Threshold = Threshold;
    }


}