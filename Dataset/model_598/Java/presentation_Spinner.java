





import java.util.List;
import java.util.ArrayList;

public class presentation_Spinner extends Composite {

    private String pageIncrement;
    private String minimum;
    private String selection;
    private String digits;
    private String maximum;
    private String textLimit;
    private String increment;
    private String text;



    public presentation_Spinner(
        String pageIncrement,        String minimum,        String selection,        String digits,        String maximum,        String textLimit,        String increment,        String text    ) {
        super(
        );
        this.pageIncrement = pageIncrement;
        this.minimum = minimum;
        this.selection = selection;
        this.digits = digits;
        this.maximum = maximum;
        this.textLimit = textLimit;
        this.increment = increment;
        this.text = text;
    }


    public String getPageincrement() {
        return pageIncrement;
    }

    public void setPageincrement(String pageIncrement) {
        this.pageIncrement = pageIncrement;
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
    public String getDigits() {
        return digits;
    }

    public void setDigits(String digits) {
        this.digits = digits;
    }
    public String getMaximum() {
        return maximum;
    }

    public void setMaximum(String maximum) {
        this.maximum = maximum;
    }
    public String getTextlimit() {
        return textLimit;
    }

    public void setTextlimit(String textLimit) {
        this.textLimit = textLimit;
    }
    public String getIncrement() {
        return increment;
    }

    public void setIncrement(String increment) {
        this.increment = increment;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }


}