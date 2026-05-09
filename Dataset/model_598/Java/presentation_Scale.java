





import java.util.List;
import java.util.ArrayList;

public class presentation_Scale extends Control {

    private String increment;
    private String selection;
    private String minimum;
    private String pageIncrement;
    private String maximum;



    public presentation_Scale(
        String increment,        String selection,        String minimum,        String pageIncrement,        String maximum    ) {
        super(
        );
        this.increment = increment;
        this.selection = selection;
        this.minimum = minimum;
        this.pageIncrement = pageIncrement;
        this.maximum = maximum;
    }


    public String getIncrement() {
        return increment;
    }

    public void setIncrement(String increment) {
        this.increment = increment;
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
    public String getPageincrement() {
        return pageIncrement;
    }

    public void setPageincrement(String pageIncrement) {
        this.pageIncrement = pageIncrement;
    }
    public String getMaximum() {
        return maximum;
    }

    public void setMaximum(String maximum) {
        this.maximum = maximum;
    }


}