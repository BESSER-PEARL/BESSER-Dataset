





import java.util.List;
import java.util.ArrayList;

public class tracker_MilkTest extends Event {

    private float percentButterFat;
    private int somaticCellCounts;
    private float poundsProduced;
    private float otherSolids;
    private float percentProtein;



    public tracker_MilkTest(
        float percentButterFat,        int somaticCellCounts,        float poundsProduced,        float otherSolids,        float percentProtein    ) {
        super(
        );
        this.percentButterFat = percentButterFat;
        this.somaticCellCounts = somaticCellCounts;
        this.poundsProduced = poundsProduced;
        this.otherSolids = otherSolids;
        this.percentProtein = percentProtein;
    }


    public float getPercentbutterfat() {
        return percentButterFat;
    }

    public void setPercentbutterfat(float percentButterFat) {
        this.percentButterFat = percentButterFat;
    }
    public int getSomaticcellcounts() {
        return somaticCellCounts;
    }

    public void setSomaticcellcounts(int somaticCellCounts) {
        this.somaticCellCounts = somaticCellCounts;
    }
    public float getPoundsproduced() {
        return poundsProduced;
    }

    public void setPoundsproduced(float poundsProduced) {
        this.poundsProduced = poundsProduced;
    }
    public float getOthersolids() {
        return otherSolids;
    }

    public void setOthersolids(float otherSolids) {
        this.otherSolids = otherSolids;
    }
    public float getPercentprotein() {
        return percentProtein;
    }

    public void setPercentprotein(float percentProtein) {
        this.percentProtein = percentProtein;
    }


}