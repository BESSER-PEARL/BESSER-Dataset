





import java.util.List;
import java.util.ArrayList;

public class shr5Management_TrainingRate extends RangeTableEntry {

    private String timeUnit;
    private int factor;



    public shr5Management_TrainingRate(
        String timeUnit,        int factor    ) {
        super(
        );
        this.timeUnit = timeUnit;
        this.factor = factor;
    }


    public String getTimeunit() {
        return timeUnit;
    }

    public void setTimeunit(String timeUnit) {
        this.timeUnit = timeUnit;
    }
    public int getFactor() {
        return factor;
    }

    public void setFactor(int factor) {
        this.factor = factor;
    }


}