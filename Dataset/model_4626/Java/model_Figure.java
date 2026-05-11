





import java.util.List;
import java.util.ArrayList;

public class model_Figure extends Primitive {

    private String toolTip;
    private String onMouseIn;
    private String onMouseOut;
    private String onDoubleClick;
    private boolean visible;
    private String border;
    private String foregroundColor;
    private String onMouseDrag;
    private String onMouseHover;
    private String onMouseMove;
    private String backgroundColor;
    private String opaque;
    private String onClick;



    public model_Figure(
        String toolTip,        String onMouseIn,        String onMouseOut,        String onDoubleClick,        boolean visible,        String border,        String foregroundColor,        String onMouseDrag,        String onMouseHover,        String onMouseMove,        String backgroundColor,        String opaque,        String onClick    ) {
        super(
        );
        this.toolTip = toolTip;
        this.onMouseIn = onMouseIn;
        this.onMouseOut = onMouseOut;
        this.onDoubleClick = onDoubleClick;
        this.visible = visible;
        this.border = border;
        this.foregroundColor = foregroundColor;
        this.onMouseDrag = onMouseDrag;
        this.onMouseHover = onMouseHover;
        this.onMouseMove = onMouseMove;
        this.backgroundColor = backgroundColor;
        this.opaque = opaque;
        this.onClick = onClick;
    }


    public String getTooltip() {
        return toolTip;
    }

    public void setTooltip(String toolTip) {
        this.toolTip = toolTip;
    }
    public String getOnmousein() {
        return onMouseIn;
    }

    public void setOnmousein(String onMouseIn) {
        this.onMouseIn = onMouseIn;
    }
    public String getOnmouseout() {
        return onMouseOut;
    }

    public void setOnmouseout(String onMouseOut) {
        this.onMouseOut = onMouseOut;
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
    public String getOnmousedrag() {
        return onMouseDrag;
    }

    public void setOnmousedrag(String onMouseDrag) {
        this.onMouseDrag = onMouseDrag;
    }
    public String getOnmousehover() {
        return onMouseHover;
    }

    public void setOnmousehover(String onMouseHover) {
        this.onMouseHover = onMouseHover;
    }
    public String getOnmousemove() {
        return onMouseMove;
    }

    public void setOnmousemove(String onMouseMove) {
        this.onMouseMove = onMouseMove;
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
    public String getOnclick() {
        return onClick;
    }

    public void setOnclick(String onClick) {
        this.onClick = onClick;
    }


}