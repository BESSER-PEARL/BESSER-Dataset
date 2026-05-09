





import java.util.List;
import java.util.ArrayList;

public class presentation_Scale extends Control {

    private String maximum;
    private String increment;
    private String minimum;
    private String pageIncrement;
    private String selection;



    public presentation_Scale(
        String maximum,        String increment,        String minimum,        String pageIncrement,        String selection    ) {
        super(
        );
        this.maximum = maximum;
        this.increment = increment;
        this.minimum = minimum;
        this.pageIncrement = pageIncrement;
        this.selection = selection;
    }


    public String getMaximum() {
        return maximum;
    }

    public void setMaximum(String maximum) {
        this.maximum = maximum;
    }
    public String getIncrement() {
        return increment;
    }

    public void setIncrement(String increment) {
        this.increment = increment;
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
    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }


}