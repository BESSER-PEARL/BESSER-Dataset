





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_Figure extends Primitive {

    private String backgroundColor;
    private String border;
    private String foregroundColor;
    private String opaque;
    private String onDoubleClick;
    private boolean visible;
    private String onClick;
    private String toolTip;





    private VisualInterface_Cursor visualinterface_cursor;




    private VisualInterface_Dimension visualinterface_dimension;


    public VisualInterface_Figure(
        String backgroundColor,        String border,        String foregroundColor,        String opaque,        String onDoubleClick,        boolean visible,        String onClick,        String toolTip    ) {
        super(
        );
        this.backgroundColor = backgroundColor;
        this.border = border;
        this.foregroundColor = foregroundColor;
        this.opaque = opaque;
        this.onDoubleClick = onDoubleClick;
        this.visible = visible;
        this.onClick = onClick;
        this.toolTip = toolTip;
    }


    public String getBackgroundcolor() {
        return backgroundColor;
    }

    public void setBackgroundcolor(String backgroundColor) {
        this.backgroundColor = backgroundColor;
    }
    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }
    public String getForegroundcolor() {
        return foregroundColor;
    }

    public void setForegroundcolor(String foregroundColor) {
        this.foregroundColor = foregroundColor;
    }
    public String getOpaque() {
        return opaque;
    }

    public void setOpaque(String opaque) {
        this.opaque = opaque;
    }
    public String getOndoubleclick() {
        return onDoubleClick;
    }

    public void setOndoubleclick(String onDoubleClick) {
        this.onDoubleClick = onDoubleClick;
    }
    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }
    public String getOnclick() {
        return onClick;
    }

    public void setOnclick(String onClick) {
        this.onClick = onClick;
    }
    public String getTooltip() {
        return toolTip;
    }

    public void setTooltip(String toolTip) {
        this.toolTip = toolTip;
    }

    public VisualInterface_Cursor getVisualinterface_cursor() {
        return visualinterface_cursor;
    }

    public void setVisualinterface_cursor(VisualInterface_Cursor visualinterface_cursor) {
        this.visualinterface_cursor = visualinterface_cursor;
    }
    public VisualInterface_Dimension getVisualinterface_dimension() {
        return visualinterface_dimension;
    }

    public void setVisualinterface_dimension(VisualInterface_Dimension visualinterface_dimension) {
        this.visualinterface_dimension = visualinterface_dimension;
    }

}