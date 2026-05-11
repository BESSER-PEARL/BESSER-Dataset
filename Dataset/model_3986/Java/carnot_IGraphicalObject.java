





import java.util.List;
import java.util.ArrayList;

public class carnot_IGraphicalObject extends IModelElement {

    private String borderColor;
    private String fillColor;
    private String style;



    public carnot_IGraphicalObject(
        String borderColor,        String fillColor,        String style    ) {
        super(
        );
        this.borderColor = borderColor;
        this.fillColor = fillColor;
        this.style = style;
    }


    public String getBordercolor() {
        return borderColor;
    }

    public void setBordercolor(String borderColor) {
        this.borderColor = borderColor;
    }
    public String getFillcolor() {
        return fillColor;
    }

    public void setFillcolor(String fillColor) {
        this.fillColor = fillColor;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }


}