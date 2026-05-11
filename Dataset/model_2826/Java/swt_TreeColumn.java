





import java.util.List;
import java.util.ArrayList;

public class swt_TreeColumn extends Item {

    private String toolTipText;
    private String displayText;



    public swt_TreeColumn(
        String toolTipText,        String displayText    ) {
        super(
        );
        this.toolTipText = toolTipText;
        this.displayText = displayText;
    }


    public String getTooltiptext() {
        return toolTipText;
    }

    public void setTooltiptext(String toolTipText) {
        this.toolTipText = toolTipText;
    }
    public String getDisplaytext() {
        return displayText;
    }

    public void setDisplaytext(String displayText) {
        this.displayText = displayText;
    }


}