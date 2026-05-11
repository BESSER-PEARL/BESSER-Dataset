





import java.util.List;
import java.util.ArrayList;

public class website_NamedDisplayElement extends NamedElement {

    private String displayLabel;



    public website_NamedDisplayElement(
        String displayLabel    ) {
        super(
        );
        this.displayLabel = displayLabel;
    }


    public String getDisplaylabel() {
        return displayLabel;
    }

    public void setDisplaylabel(String displayLabel) {
        this.displayLabel = displayLabel;
    }


}