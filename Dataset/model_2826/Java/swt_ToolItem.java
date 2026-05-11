





import java.util.List;
import java.util.ArrayList;

public class swt_ToolItem extends Item {

    private String toolTipText;
    private String hotImage;
    private boolean selection;
    private boolean enabled;





    private swt_ToolBar swt_toolbar;




    private swt_ToolBar swt_toolbar;


    public swt_ToolItem(
        String toolTipText,        String hotImage,        boolean selection,        boolean enabled    ) {
        super(
        );
        this.toolTipText = toolTipText;
        this.hotImage = hotImage;
        this.selection = selection;
        this.enabled = enabled;
    }


    public String getTooltiptext() {
        return toolTipText;
    }

    public void setTooltiptext(String toolTipText) {
        this.toolTipText = toolTipText;
    }
    public String getHotimage() {
        return hotImage;
    }

    public void setHotimage(String hotImage) {
        this.hotImage = hotImage;
    }
    public boolean getSelection() {
        return selection;
    }

    public void setSelection(boolean selection) {
        this.selection = selection;
    }
    public boolean getEnabled() {
        return enabled;
    }

    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
    }

    public swt_ToolBar getSwt_toolbar() {
        return swt_toolbar;
    }

    public void setSwt_toolbar(swt_ToolBar swt_toolbar) {
        this.swt_toolbar = swt_toolbar;
    }
    public swt_ToolBar getSwt_toolbar() {
        return swt_toolbar;
    }

    public void setSwt_toolbar(swt_ToolBar swt_toolbar) {
        this.swt_toolbar = swt_toolbar;
    }

}