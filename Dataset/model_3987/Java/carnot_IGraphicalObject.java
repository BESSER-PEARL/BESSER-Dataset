





import java.util.List;
import java.util.ArrayList;

public class carnot_IGraphicalObject extends IModelElement {

    private String borderColor;
    private String style;
    private String fillColor;



    public carnot_IGraphicalObject(
        String borderColor,        String style,        String fillColor    ) {
        super(
        );
        this.borderColor = borderColor;
        this.style = style;
        this.fillColor = fillColor;
    }


    public String getBordercolor() {
        return borderColor;
    }

    public void setBordercolor(String borderColor) {
        this.borderColor = borderColor;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getFillcolor() {
        return fillColor;
    }

    public void setFillcolor(String fillColor) {
        this.fillColor = fillColor;
    }


}