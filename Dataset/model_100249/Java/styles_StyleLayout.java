





import java.util.List;
import java.util.ArrayList;

public class styles_StyleLayout  {

    private String fontName;
    private float transparency;
    private int fontSize;
    private int lineWidth;
    private String gradient_orientation;
    private String fontItalic;
    private String fontBold;
    private String lineStyle;





    private styles_ColorOrGradient styles_colororgradient;




    private styles_HighlightingValues styles_highlightingvalues;




    private styles_Style styles_style;


    public styles_StyleLayout(
        String fontName,        float transparency,        int fontSize,        int lineWidth,        String gradient_orientation,        String fontItalic,        String fontBold,        String lineStyle    ) {
        this.fontName = fontName;
        this.transparency = transparency;
        this.fontSize = fontSize;
        this.lineWidth = lineWidth;
        this.gradient_orientation = gradient_orientation;
        this.fontItalic = fontItalic;
        this.fontBold = fontBold;
        this.lineStyle = lineStyle;
    }


    public String getFontname() {
        return fontName;
    }

    public void setFontname(String fontName) {
        this.fontName = fontName;
    }
    public float getTransparency() {
        return transparency;
    }

    public void setTransparency(float transparency) {
        this.transparency = transparency;
    }
    public int getFontsize() {
        return fontSize;
    }

    public void setFontsize(int fontSize) {
        this.fontSize = fontSize;
    }
    public int getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(int lineWidth) {
        this.lineWidth = lineWidth;
    }
    public String getGradient_orientation() {
        return gradient_orientation;
    }

    public void setGradient_orientation(String gradient_orientation) {
        this.gradient_orientation = gradient_orientation;
    }
    public String getFontitalic() {
        return fontItalic;
    }

    public void setFontitalic(String fontItalic) {
        this.fontItalic = fontItalic;
    }
    public String getFontbold() {
        return fontBold;
    }

    public void setFontbold(String fontBold) {
        this.fontBold = fontBold;
    }
    public String getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(String lineStyle) {
        this.lineStyle = lineStyle;
    }

    public styles_ColorOrGradient getStyles_colororgradient() {
        return styles_colororgradient;
    }

    public void setStyles_colororgradient(styles_ColorOrGradient styles_colororgradient) {
        this.styles_colororgradient = styles_colororgradient;
    }
    public styles_HighlightingValues getStyles_highlightingvalues() {
        return styles_highlightingvalues;
    }

    public void setStyles_highlightingvalues(styles_HighlightingValues styles_highlightingvalues) {
        this.styles_highlightingvalues = styles_highlightingvalues;
    }
    public styles_Style getStyles_style() {
        return styles_style;
    }

    public void setStyles_style(styles_Style styles_style) {
        this.styles_style = styles_style;
    }

}