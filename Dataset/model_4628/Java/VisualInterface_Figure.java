





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_Figure extends Primitive {

    private String toolTip;
    private boolean visible;
    private String foregroundColor;
    private String border;
    private String onClick;
    private String onDoubleClick;
    private String backgroundColor;
    private String opaque;





    private VisualInterface_Dimension visualinterface_dimension;


    public VisualInterface_Figure(
        String toolTip,        boolean visible,        String foregroundColor,        String border,        String onClick,        String onDoubleClick,        String backgroundColor,        String opaque    ) {
        super(
        );
        this.toolTip = toolTip;
        this.visible = visible;
        this.foregroundColor = foregroundColor;
        this.border = border;
        this.onClick = onClick;
        this.onDoubleClick = onDoubleClick;
        this.backgroundColor = backgroundColor;
        this.opaque = opaque;
    }


    public String getTooltip() {
        return toolTip;
    }

    public void setTooltip(String toolTip) {
        this.toolTip = toolTip;
    }
    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }
    public String getForegroundcolor() {
        return foregroundColor;
    }

    public void setForegroundcolor(String foregroundColor) {
        this.foregroundColor = foregroundColor;
    }
    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }
    public String getOnclick() {
        return onClick;
    }

    public void setOnclick(String onClick) {
        this.onClick = onClick;
    }
    public String getOndoubleclick() {
        return onDoubleClick;
    }

    public void setOndoubleclick(String onDoubleClick) {
        this.onDoubleClick = onDoubleClick;
    }
    public String getBackgroundcolor() {
        return backgroundColor;
    }

    public void setBackgroundcolor(String backgroundColor) {
        this.backgroundColor = backgroundColor;
    }
    public String getOpaque() {
        return opaque;
    }

    public void setOpaque(String opaque) {
        this.opaque = opaque;
    }

    public VisualInterface_Dimension getVisualinterface_dimension() {
        return visualinterface_dimension;
    }

    public void setVisualinterface_dimension(VisualInterface_Dimension visualinterface_dimension) {
        this.visualinterface_dimension = visualinterface_dimension;
    }

}