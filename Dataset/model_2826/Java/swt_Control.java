





import java.util.List;
import java.util.ArrayList;

public class swt_Control extends Widget {

    private String borderStyle;
    private String textOrientationStyle;
    private boolean visible;
    private String size;
    private boolean touchEnabled;
    private String toolTipText;
    private boolean enabled;





    private swt_FormAttachment swt_formattachment;




    private swt_TabItem swt_tabitem;




    private swt_Font swt_font;




    private swt_Color swt_color;




    private swt_LayoutData swt_layoutdata;


    public swt_Control(
        String borderStyle,        String textOrientationStyle,        boolean visible,        String size,        boolean touchEnabled,        String toolTipText,        boolean enabled    ) {
        super(
        );
        this.borderStyle = borderStyle;
        this.textOrientationStyle = textOrientationStyle;
        this.visible = visible;
        this.size = size;
        this.touchEnabled = touchEnabled;
        this.toolTipText = toolTipText;
        this.enabled = enabled;
    }


    public String getBorderstyle() {
        return borderStyle;
    }

    public void setBorderstyle(String borderStyle) {
        this.borderStyle = borderStyle;
    }
    public String getTextorientationstyle() {
        return textOrientationStyle;
    }

    public void setTextorientationstyle(String textOrientationStyle) {
        this.textOrientationStyle = textOrientationStyle;
    }
    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public boolean getTouchenabled() {
        return touchEnabled;
    }

    public void setTouchenabled(boolean touchEnabled) {
        this.touchEnabled = touchEnabled;
    }
    public String getTooltiptext() {
        return toolTipText;
    }

    public void setTooltiptext(String toolTipText) {
        this.toolTipText = toolTipText;
    }
    public boolean getEnabled() {
        return enabled;
    }

    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
    }

    public swt_FormAttachment getSwt_formattachment() {
        return swt_formattachment;
    }

    public void setSwt_formattachment(swt_FormAttachment swt_formattachment) {
        this.swt_formattachment = swt_formattachment;
    }
    public swt_TabItem getSwt_tabitem() {
        return swt_tabitem;
    }

    public void setSwt_tabitem(swt_TabItem swt_tabitem) {
        this.swt_tabitem = swt_tabitem;
    }
    public swt_Font getSwt_font() {
        return swt_font;
    }

    public void setSwt_font(swt_Font swt_font) {
        this.swt_font = swt_font;
    }
    public swt_Color getSwt_color() {
        return swt_color;
    }

    public void setSwt_color(swt_Color swt_color) {
        this.swt_color = swt_color;
    }
    public swt_LayoutData getSwt_layoutdata() {
        return swt_layoutdata;
    }

    public void setSwt_layoutdata(swt_LayoutData swt_layoutdata) {
        this.swt_layoutdata = swt_layoutdata;
    }

}