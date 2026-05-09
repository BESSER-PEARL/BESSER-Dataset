





import java.util.List;
import java.util.ArrayList;

public class presentation_ProgressBar extends Control {

    private String state;
    private String selection;
    private String minimum;
    private String maximum;



    public presentation_ProgressBar(
        String state,        String selection,        String minimum,        String maximum    ) {
        super(
        );
        this.state = state;
        this.selection = selection;
        this.minimum = minimum;
        this.maximum = maximum;
    }


    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }
    public String getMinimum() {
        return minimum;
    }

    public void setMinimum(String minimum) {
        this.minimum = minimum;
    }
    public String getMaximum() {
        return maximum;
    }

    public void setMaximum(String maximum) {
        this.maximum = maximum;
    }


}