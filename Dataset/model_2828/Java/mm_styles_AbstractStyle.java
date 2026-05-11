





import java.util.List;
import java.util.ArrayList;

public class mm_styles_AbstractStyle  {

    private String filled;
    private String lineStyle;
    private String lineVisible;
    private String lineWidth;
    private String transparency;





    private styles_Color styles_color;




    private styles_Color styles_color;


    public mm_styles_AbstractStyle(
        String filled,        String lineStyle,        String lineVisible,        String lineWidth,        String transparency    ) {
        this.filled = filled;
        this.lineStyle = lineStyle;
        this.lineVisible = lineVisible;
        this.lineWidth = lineWidth;
        this.transparency = transparency;
    }


    public String getFilled() {
        return filled;
    }

    public void setFilled(String filled) {
        this.filled = filled;
    }
    public String getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(String lineStyle) {
        this.lineStyle = lineStyle;
    }
    public String getLinevisible() {
        return lineVisible;
    }

    public void setLinevisible(String lineVisible) {
        this.lineVisible = lineVisible;
    }
    public String getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(String lineWidth) {
        this.lineWidth = lineWidth;
    }
    public String getTransparency() {
        return transparency;
    }

    public void setTransparency(String transparency) {
        this.transparency = transparency;
    }

    public styles_Color getStyles_color() {
        return styles_color;
    }

    public void setStyles_color(styles_Color styles_color) {
        this.styles_color = styles_color;
    }
    public styles_Color getStyles_color() {
        return styles_color;
    }

    public void setStyles_color(styles_Color styles_color) {
        this.styles_color = styles_color;
    }

}