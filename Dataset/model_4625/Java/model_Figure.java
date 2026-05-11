





import java.util.List;
import java.util.ArrayList;

public class model_Figure extends Primitive {

    private String border;
    private String onMouseIn;
    private boolean visible;
    private String opaque;
    private String onMouseDrag;
    private String onMouseHover;
    private String backgroundColor;
    private String onClick;
    private String toolTip;
    private String onMouseMove;
    private String onDoubleClick;
    private String onMouseOut;
    private String foregroundColor;





    private model_Dimension model_dimension;




    private model_Cursor model_cursor;


    public model_Figure(
        String border,        String onMouseIn,        boolean visible,        String opaque,        String onMouseDrag,        String onMouseHover,        String backgroundColor,        String onClick,        String toolTip,        String onMouseMove,        String onDoubleClick,        String onMouseOut,        String foregroundColor    ) {
        super(
        );
        this.border = border;
        this.onMouseIn = onMouseIn;
        this.visible = visible;
        this.opaque = opaque;
        this.onMouseDrag = onMouseDrag;
        this.onMouseHover = onMouseHover;
        this.backgroundColor = backgroundColor;
        this.onClick = onClick;
        this.toolTip = toolTip;
        this.onMouseMove = onMouseMove;
        this.onDoubleClick = onDoubleClick;
        this.onMouseOut = onMouseOut;
        this.foregroundColor = foregroundColor;
    }


    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }
    public String getOnmousein() {
        return onMouseIn;
    }

    public void setOnmousein(String onMouseIn) {
        this.onMouseIn = onMouseIn;
    }
    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }
    public String getOpaque() {
        return opaque;
    }

    public void setOpaque(String opaque) {
        this.opaque = opaque;
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
    public String getBackgroundcolor() {
        return backgroundColor;
    }

    public void setBackgroundcolor(String backgroundColor) {
        this.backgroundColor = backgroundColor;
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
    public String getOnmousemove() {
        return onMouseMove;
    }

    public void setOnmousemove(String onMouseMove) {
        this.onMouseMove = onMouseMove;
    }
    public String getOndoubleclick() {
        return onDoubleClick;
    }

    public void setOndoubleclick(String onDoubleClick) {
        this.onDoubleClick = onDoubleClick;
    }
    public String getOnmouseout() {
        return onMouseOut;
    }

    public void setOnmouseout(String onMouseOut) {
        this.onMouseOut = onMouseOut;
    }
    public String getForegroundcolor() {
        return foregroundColor;
    }

    public void setForegroundcolor(String foregroundColor) {
        this.foregroundColor = foregroundColor;
    }

    public model_Dimension getModel_dimension() {
        return model_dimension;
    }

    public void setModel_dimension(model_Dimension model_dimension) {
        this.model_dimension = model_dimension;
    }
    public model_Cursor getModel_cursor() {
        return model_cursor;
    }

    public void setModel_cursor(model_Cursor model_cursor) {
        this.model_cursor = model_cursor;
    }

}