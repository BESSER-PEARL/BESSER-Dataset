





import java.util.List;
import java.util.ArrayList;

public class synccharts_Action extends Annotatable {

    private boolean isImmediate;
    private int delay;
    private String label;



    public synccharts_Action(
        boolean isImmediate,        int delay,        String label    ) {
        super(
        );
        this.isImmediate = isImmediate;
        this.delay = delay;
        this.label = label;
    }


    public boolean getIsimmediate() {
        return isImmediate;
    }

    public void setIsimmediate(boolean isImmediate) {
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


}