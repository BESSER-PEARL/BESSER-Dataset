





import java.util.List;
import java.util.ArrayList;

public class dbmddandroid_Relation  {

    private int minTargetMultiplicity;
    private int minSourceMultiplicity;
    private int maxTargetMultiplicity;
    private int maxSourceMultiplicity;



    public dbmddandroid_Relation(
        int minTargetMultiplicity,        int minSourceMultiplicity,        int maxTargetMultiplicity,        int maxSourceMultiplicity    ) {
        this.minTargetMultiplicity = minTargetMultiplicity;
        this.minSourceMultiplicity = minSourceMultiplicity;
        this.maxTargetMultiplicity = maxTargetMultiplicity;
        this.maxSourceMultiplicity = maxSourceMultiplicity;
    }


    public int getMintargetmultiplicity() {
        return minTargetMultiplicity;
    }

    public void setMintargetmultiplicity(int minTargetMultiplicity) {
        this.minTargetMultiplicity = minTargetMultiplicity;
    }
    public int getMinsourcemultiplicity() {
        return minSourceMultiplicity;
    }

    public void setMinsourcemultiplicity(int minSourceMultiplicity) {
        this.minSourceMultiplicity = minSourceMultiplicity;
    }
    public int getMaxtargetmultiplicity() {
        return maxTargetMultiplicity;
    }

    public void setMaxtargetmultiplicity(int maxTargetMultiplicity) {
        this.maxTargetMultiplicity = maxTargetMultiplicity;
    }
    public int getMaxsourcemultiplicity() {
        return maxSourceMultiplicity;
    }

    public void setMaxsourcemultiplicity(int maxSourceMultiplicity) {
        this.maxSourceMultiplicity = maxSourceMultiplicity;
    }


}