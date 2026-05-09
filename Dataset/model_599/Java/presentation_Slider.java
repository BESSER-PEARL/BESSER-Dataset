





import java.util.List;
import java.util.ArrayList;

public class presentation_Slider extends Control {

    private String pageIncrement;
    private String maximum;
    private String thumb;
    private String increment;
    private String minimum;
    private String selection;



    public presentation_Slider(
        String pageIncrement,        String maximum,        String thumb,        String increment,        String minimum,        String selection    ) {
        super(
        );
        this.pageIncrement = pageIncrement;
        this.maximum = maximum;
        this.thumb = thumb;
        this.increment = increment;
        this.minimum = minimum;
        this.selection = selection;
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
    public String getThumb() {
        return thumb;
    }

    public void setThumb(String thumb) {
        this.thumb = thumb;
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
    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }


}