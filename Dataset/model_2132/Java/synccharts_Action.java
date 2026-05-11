





import java.util.List;
import java.util.ArrayList;

public class synccharts_Action extends Annotatable {

    private int delay;
    private String label;
    private boolean isImmediate;



    public synccharts_Action(
        int delay,        String label,        boolean isImmediate    ) {
        super(
        );
        this.delay = delay;
        this.label = label;
        this.isImmediate = isImmediate;
    }


    public int getDelay() {
        return delay;
    }

    public void setDelay(int delay) {
        this.delay = delay;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public boolean getIsimmediate() {
        return isImmediate;
    }

    public void setIsimmediate(boolean isImmediate) {
        this.isImmediate = isImmediate;
    }


}