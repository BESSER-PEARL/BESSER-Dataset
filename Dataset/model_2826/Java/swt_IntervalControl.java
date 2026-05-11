





import java.util.List;
import java.util.ArrayList;

public class swt_IntervalControl extends Control {

    private int maximum;
    private int selection;
    private int minimum;



    public swt_IntervalControl(
        int maximum,        int selection,        int minimum    ) {
        super(
        );
        this.maximum = maximum;
        this.selection = selection;
        this.minimum = minimum;
    }


    public int getMaximum() {
        return maximum;
    }

    public void setMaximum(int maximum) {
        this.maximum = maximum;
    }
    public int getSelection() {
        return selection;
    }

    public void setSelection(int selection) {
        this.selection = selection;
    }
    public int getMinimum() {
        return minimum;
    }

    public void setMinimum(int minimum) {
        this.minimum = minimum;
    }


}