





import java.util.List;
import java.util.ArrayList;

public class synccharts_Action extends Annotatable {

    private int delay;
    private boolean isImmediate;
    private String label;



    public synccharts_Action(
        int delay,        boolean isImmediate,        String label    ) {
        super(
        );
        this.delay = delay;
        this.isImmediate = isImmediate;
        this.label = label;
    }


    public int getDelay() {
        return delay;
    }

    public void setDelay(int delay) {
        this.delay = delay;
    }
    public boolean getIsimmediate() {
        return isImmediate;
    }

    public void setIsimmediate(boolean isImmediate) {
        this.isImmediate = isImmediate;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }


}