





import java.util.List;
import java.util.ArrayList;

public class presentation_Slider extends Control {

    private String minimum;
    private String pageIncrement;
    private String selection;
    private String thumb;
    private String maximum;
    private String increment;



    public presentation_Slider(
        String minimum,        String pageIncrement,        String selection,        String thumb,        String maximum,        String increment    ) {
        super(
        );
        this.minimum = minimum;
        this.pageIncrement = pageIncrement;
        this.selection = selection;
        this.thumb = thumb;
        this.maximum = maximum;
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
    public String getThumb() {
        return thumb;
    }

    public void setThumb(String thumb) {
        this.thumb = thumb;
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


}