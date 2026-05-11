





import java.util.List;
import java.util.ArrayList;

public class model_Figure extends Primitive {

    private String backgroundColor;
    private String onMouseIn;
    private String opaque;
    private String onMouseHover;
    private String toolTip;
    private String onClick;
    private String border;
    private String onMouseOut;
    private String onDoubleClick;
    private String foregroundColor;
    private String onMouseDrag;
    private String onMouseMove;
    private boolean visible;



    public model_Figure(
        String backgroundColor,        String onMouseIn,        String opaque,        String onMouseHover,        String toolTip,        String onClick,        String border,        String onMouseOut,        String onDoubleClick,        String foregroundColor,        String onMouseDrag,        String onMouseMove,        boolean visible    ) {
        super(
        );
        this.backgroundColor = backgroundColor;
        this.onMouseIn = onMouseIn;
        this.opaque = opaque;
        this.onMouseHover = onMouseHover;
        this.toolTip = toolTip;
        this.onClick = onClick;
        this.border = border;
        this.onMouseOut = onMouseOut;
        this.onDoubleClick = onDoubleClick;
        this.foregroundColor = foregroundColor;
        this.onMouseDrag = onMouseDrag;
        this.onMouseMove = onMouseMove;
        this.visible = visible;
    }


    public String getBackgroundcolor() {
        return backgroundColor;
    }

    public void setBackgroundcolor(String backgroundColor) {
        this.backgroundColor = backgroundColor;
    }
    public String getOnmousein() {
        return onMouseIn;
    }

    public void setOnmousein(String onMouseIn) {
        this.onMouseIn = onMouseIn;
    }
    public String getOpaque() {
        return opaque;
    }

    public void setOpaque(String opaque) {
        this.opaque = opaque;
    }
    public String getOnmousehover() {
        return onMouseHover;
    }

    public void setOnmousehover(String onMouseHover) {
        this.onMouseHover = onMouseHover;
    }
    public String getTooltip() {
        return toolTip;
    }

    public void setTooltip(String toolTip) {
        this.toolTip = toolTip;
    }
    public String getOnclick() {
        return onClick;
    }

    public void setOnclick(String onClick) {
        this.onClick = onClick;
    }
    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
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
    public String getOnmousemove() {
        return onMouseMove;
    }

    public void setOnmousemove(String onMouseMove) {
        this.onMouseMove = onMouseMove;
    }
    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }


}