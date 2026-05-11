





import java.util.List;
import java.util.ArrayList;

public class dg_Style  {

    private String fontName;
    private String strokeDashLength;
    private String strokeWidth;
    private String fontDecoration;
    private String strokeOpacity;
    private String fillOpacity;
    private String fontSize;
    private String fontBold;
    private String fontItalic;





    private dg_GraphicalElement dg_graphicalelement;


    public dg_Style(
        String fontName,        String strokeDashLength,        String strokeWidth,        String fontDecoration,        String strokeOpacity,        String fillOpacity,        String fontSize,        String fontBold,        String fontItalic    ) {
        this.fontName = fontName;
        this.strokeDashLength = strokeDashLength;
        this.strokeWidth = strokeWidth;
        this.fontDecoration = fontDecoration;
        this.strokeOpacity = strokeOpacity;
        this.fillOpacity = fillOpacity;
        this.fontSize = fontSize;
        this.fontBold = fontBold;
        this.fontItalic = fontItalic;
    }


    public String getFontname() {
        return fontName;
    }

    public void setFontname(String fontName) {
        this.fontName = fontName;
    }
    public String getStrokedashlength() {
        return strokeDashLength;
    }

    public void setStrokedashlength(String strokeDashLength) {
        this.strokeDashLength = strokeDashLength;
    }
    public String getStrokewidth() {
        return strokeWidth;
    }

    public void setStrokewidth(String strokeWidth) {
        this.strokeWidth = strokeWidth;
    }
    public String getFontdecoration() {
        return fontDecoration;
    }

    public void setFontdecoration(String fontDecoration) {
        this.fontDecoration = fontDecoration;
    }
    public String getStrokeopacity() {
        return strokeOpacity;
    }

    public void setStrokeopacity(String strokeOpacity) {
        this.strokeOpacity = strokeOpacity;
    }
    public String getFillopacity() {
        return fillOpacity;
    }

    public void setFillopacity(String fillOpacity) {
        this.fillOpacity = fillOpacity;
    }
    public String getFontsize() {
        return fontSize;
    }

    public void setFontsize(String fontSize) {
        this.fontSize = fontSize;
    }
    public String getFontbold() {
        return fontBold;
    }

    public void setFontbold(String fontBold) {
        this.fontBold = fontBold;
    }
    public String getFontitalic() {
        return fontItalic;
    }

    public void setFontitalic(String fontItalic) {
        this.fontItalic = fontItalic;
    }

    public dg_GraphicalElement getDg_graphicalelement() {
        return dg_graphicalelement;
    }

    public void setDg_graphicalelement(dg_GraphicalElement dg_graphicalelement) {
        this.dg_graphicalelement = dg_graphicalelement;
    }

}