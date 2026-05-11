





import java.util.List;
import java.util.ArrayList;

public class swt_TabItem extends Item {

    private String toolTipText;





    private swt_TabFolder swt_tabfolder;


    public swt_TabItem(
        String toolTipText    ) {
        super(
        );
        this.toolTipText = toolTipText;
    }


    public String getTooltiptext() {
        return toolTipText;
    }

    public void setTooltiptext(String toolTipText) {
        this.toolTipText = toolTipText;
    }

    public swt_TabFolder getSwt_tabfolder() {
        return swt_tabfolder;
    }

    public void setSwt_tabfolder(swt_TabFolder swt_tabfolder) {
        this.swt_tabfolder = swt_tabfolder;
    }

}