





import java.util.List;
import java.util.ArrayList;

public class oaam_library_TaskOutputTrigger extends OaamBaseElementA {

    private float fixedRate;
    private boolean isFixedRate;



    public oaam_library_TaskOutputTrigger(
        float fixedRate,        boolean isFixedRate    ) {
        super(
        );
        this.fixedRate = fixedRate;
        this.isFixedRate = isFixedRate;
    }


    public float getFixedrate() {
        return fixedRate;
    }

    public void setFixedrate(float fixedRate) {
        this.fixedRate = fixedRate;
    }
    public boolean getIsfixedrate() {
        return isFixedRate;
    }

    public void setIsfixedrate(boolean isFixedRate) {
        this.isFixedRate = isFixedRate;
    }


}