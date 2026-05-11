





import java.util.List;
import java.util.ArrayList;

public class mm_styles_AbstractStyle  {

    private String lineVisible;
    private String lineWidth;
    private String transparency;
    private String filled;
    private String lineStyle;





    private styles_RenderingStyle styles_renderingstyle;




    private styles_Color styles_color;




    private styles_Color styles_color;


    public mm_styles_AbstractStyle(
        String lineVisible,        String lineWidth,        String transparency,        String filled,        String lineStyle    ) {
        this.lineVisible = lineVisible;
        this.lineWidth = lineWidth;
        this.transparency = transparency;
        this.filled = filled;
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

    public styles_RenderingStyle getStyles_renderingstyle() {
        return styles_renderingstyle;
    }

    public void setStyles_renderingstyle(styles_RenderingStyle styles_renderingstyle) {
        this.styles_renderingstyle = styles_renderingstyle;
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