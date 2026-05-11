





import java.util.List;
import java.util.ArrayList;

public class tracker_MilkTest extends Event {

    private float otherSolids;
    private int somaticCellCounts;
    private float percentProtein;
    private float poundsProduced;
    private float percentButterFat;



    public tracker_MilkTest(
        float otherSolids,        int somaticCellCounts,        float percentProtein,        float poundsProduced,        float percentButterFat    ) {
        super(
        );
        this.otherSolids = otherSolids;
        this.somaticCellCounts = somaticCellCounts;
        this.percentProtein = percentProtein;
        this.poundsProduced = poundsProduced;
        this.percentButterFat = percentButterFat;
    }


    public float getOthersolids() {
        return otherSolids;
    }

    public void setOthersolids(float otherSolids) {
        this.otherSolids = otherSolids;
    }
    public int getSomaticcellcounts() {
        return somaticCellCounts;
    }

    public void setSomaticcellcounts(int somaticCellCounts) {
        this.somaticCellCounts = somaticCellCounts;
    }
    public float getPercentprotein() {
        return percentProtein;
    }

    public void setPercentprotein(float percentProtein) {
        this.percentProtein = percentProtein;
    }
    public float getPoundsproduced() {
        return poundsProduced;
    }

    public void setPoundsproduced(float poundsProduced) {
        this.poundsProduced = poundsProduced;
    }
    public float getPercentbutterfat() {
        return percentButterFat;
    }

    public void setPercentbutterfat(float percentButterFat) {
        this.percentButterFat = percentButterFat;
    }


}