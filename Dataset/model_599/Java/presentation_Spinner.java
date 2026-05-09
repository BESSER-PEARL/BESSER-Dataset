





import java.util.List;
import java.util.ArrayList;

public class presentation_Spinner extends Composite {

    private String selection;
    private String maximum;
    private String text;
    private String increment;
    private String minimum;
    private String textLimit;
    private String pageIncrement;
    private String digits;



    public presentation_Spinner(
        String selection,        String maximum,        String text,        String increment,        String minimum,        String textLimit,        String pageIncrement,        String digits    ) {
        super(
        );
        this.selection = selection;
        this.maximum = maximum;
        this.text = text;
        this.increment = increment;
        this.minimum = minimum;
        this.textLimit = textLimit;
        this.pageIncrement = pageIncrement;
        this.digits = digits;
    }


    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }
    public String getMaximum() {
        return maximum;
    }

    public void setMaximum(String maximum) {
        this.maximum = maximum;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
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
    public String getTextlimit() {
        return textLimit;
    }

    public void setTextlimit(String textLimit) {
        this.textLimit = textLimit;
    }
    public String getPageincrement() {
        return pageIncrement;
    }

    public void setPageincrement(String pageIncrement) {
        this.pageIncrement = pageIncrement;
    }
    public String getDigits() {
        return digits;
    }

    public void setDigits(String digits) {
        this.digits = digits;
    }


}