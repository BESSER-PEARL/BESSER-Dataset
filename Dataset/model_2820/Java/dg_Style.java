





import java.util.List;
import java.util.ArrayList;

public class dg_Style  {

    private String fillOpacity;
    private String fontDecoration;
    private String strokeOpacity;
    private String fontSize;
    private String fontItalic;
    private String strokeDashLength;
    private String strokeWidth;
    private String fontBold;
    private String fontName;





    private dg_GraphicalElement dg_graphicalelement;


    public dg_Style(
        String fillOpacity,        String fontDecoration,        String strokeOpacity,        String fontSize,        String fontItalic,        String strokeDashLength,        String strokeWidth,        String fontBold,        String fontName    ) {
        this.fillOpacity = fillOpacity;
        this.fontDecoration = fontDecoration;
        this.strokeOpacity = strokeOpacity;
        this.fontSize = fontSize;
        this.fontItalic = fontItalic;
        this.strokeDashLength = strokeDashLength;
        this.strokeWidth = strokeWidth;
        this.fontBold = fontBold;
        this.fontName = fontName;
    }


    public String getFillopacity() {
        return fillOpacity;
    }

    public void setFillopacity(String fillOpacity) {
        this.fillOpacity = fillOpacity;
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
    public String getFontsize() {
        return fontSize;
    }

    public void setFontsize(String fontSize) {
        this.fontSize = fontSize;
    }
    public String getFontitalic() {
        return fontItalic;
    }

    public void setFontitalic(String fontItalic) {
        this.fontItalic = fontItalic;
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
    public String getFontbold() {
        return fontBold;
    }

    public void setFontbold(String fontBold) {
        this.fontBold = fontBold;
    }
    public String getFontname() {
        return fontName;
    }

    public void setFontname(String fontName) {
        this.fontName = fontName;
    }

    public dg_GraphicalElement getDg_graphicalelement() {
        return dg_graphicalelement;
    }

    public void setDg_graphicalelement(dg_GraphicalElement dg_graphicalelement) {
        this.dg_graphicalelement = dg_graphicalelement;
    }

}