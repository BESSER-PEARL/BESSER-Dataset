





import java.util.List;
import java.util.ArrayList;

public class requirements_RelationShip extends BasicElement {

    private int targetMax;
    private int targetMin;
    private int sourceMax;
    private int sourceMin;



    public requirements_RelationShip(
        int targetMax,        int targetMin,        int sourceMax,        int sourceMin    ) {
        super(
        );
        this.targetMax = targetMax;
        this.targetMin = targetMin;
        this.sourceMax = sourceMax;
        this.sourceMin = sourceMin;
    }


    public int getTargetmax() {
        return targetMax;
    }

    public void setTargetmax(int targetMax) {
        this.targetMax = targetMax;
    }
    public int getTargetmin() {
        return targetMin;
    }

    public void setTargetmin(int targetMin) {
        this.targetMin = targetMin;
    }
    public int getSourcemax() {
        return sourceMax;
    }

    public void setSourcemax(int sourceMax) {
        this.sourceMax = sourceMax;
    }
    public int getSourcemin() {
        return sourceMin;
    }

    public void setSourcemin(int sourceMin) {
        this.sourceMin = sourceMin;
    }


}