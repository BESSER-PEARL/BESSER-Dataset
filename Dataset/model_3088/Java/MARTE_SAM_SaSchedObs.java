





import java.util.List;
import java.util.ArrayList;

public class MARTE_SAM_SaSchedObs extends GaTimedObs {

    private String overlaps;
    private String suspentions;
    private String blockT;



    public MARTE_SAM_SaSchedObs(
        String overlaps,        String suspentions,        String blockT    ) {
        super(
        );
        this.overlaps = overlaps;
        this.suspentions = suspentions;
        this.blockT = blockT;
    }


    public String getOverlaps() {
        return overlaps;
    }

    public void setOverlaps(String overlaps) {
        this.overlaps = overlaps;
    }
    public String getSuspentions() {
        return suspentions;
    }

    public void setSuspentions(String suspentions) {
        this.suspentions = suspentions;
    }
    public String getBlockt() {
        return blockT;
    }

    public void setBlockt(String blockT) {
        this.blockT = blockT;
    }


}