





import java.util.List;
import java.util.ArrayList;

public class di_Style  {

    private String fontBold;
    private String strokeOpacity;
    private String fontUnderline;
    private String fillOpacity;
    private String fontSize;
    private String fontStrikeThrough;
    private String fontItalic;
    private String strokeWidth;
    private String fontName;
    private String strokeDashLength;





    private di_DiagramElement di_diagramelement;




    private di_DiagramElement di_diagramelement;


    public di_Style(
        String fontBold,        String strokeOpacity,        String fontUnderline,        String fillOpacity,        String fontSize,        String fontStrikeThrough,        String fontItalic,        String strokeWidth,        String fontName,        String strokeDashLength    ) {
        this.fontBold = fontBold;
        this.strokeOpacity = strokeOpacity;
        this.fontUnderline = fontUnderline;
        this.fillOpacity = fillOpacity;
        this.fontSize = fontSize;
        this.fontStrikeThrough = fontStrikeThrough;
        this.fontItalic = fontItalic;
        this.strokeWidth = strokeWidth;
        this.fontName = fontName;
        this.strokeDashLength = strokeDashLength;
    }


    public String getFontbold() {
        return fontBold;
    }

    public void setFontbold(String fontBold) {
        this.fontBold = fontBold;
    }
    public String getStrokeopacity() {
        return strokeOpacity;
    }

    public void setStrokeopacity(String strokeOpacity) {
        this.strokeOpacity = strokeOpacity;
    }
    public String getFontunderline() {
        return fontUnderline;
    }

    public void setFontunderline(String fontUnderline) {
        this.fontUnderline = fontUnderline;
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
    public String getFontstrikethrough() {
        return fontStrikeThrough;
    }

    public void setFontstrikethrough(String fontStrikeThrough) {
        this.fontStrikeThrough = fontStrikeThrough;
    }
    public String getFontitalic() {
        return fontItalic;
    }

    public void setFontitalic(String fontItalic) {
        this.fontItalic = fontItalic;
    }
    public String getStrokewidth() {
        return strokeWidth;
    }

    public void setStrokewidth(String strokeWidth) {
        this.strokeWidth = strokeWidth;
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

    public di_DiagramElement getDi_diagramelement() {
        return di_diagramelement;
    }

    public void setDi_diagramelement(di_DiagramElement di_diagramelement) {
        this.di_diagramelement = di_diagramelement;
    }
    public di_DiagramElement getDi_diagramelement() {
        return di_diagramelement;
    }

    public void setDi_diagramelement(di_DiagramElement di_diagramelement) {
        this.di_diagramelement = di_diagramelement;
    }

}