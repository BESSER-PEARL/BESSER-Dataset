





import java.util.List;
import java.util.ArrayList;

public class luniferadoc_richstring_RichStringImg extends RichStringMarkup {

    private String alt;
    private String src;
    private String width;
    private String height;





    private richstring_luniferadoc_XExpression richstring_luniferadoc_xexpression;


    public luniferadoc_richstring_RichStringImg(
        String alt,        String src,        String width,        String height    ) {
        super(
        );
        this.alt = alt;
        this.src = src;
        this.width = width;
        this.height = height;
    }


    public String getAlt() {
        return alt;
    }

    public void setAlt(String alt) {
        this.alt = alt;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }

    public richstring_luniferadoc_XExpression getRichstring_luniferadoc_xexpression() {
        return richstring_luniferadoc_xexpression;
    }

    public void setRichstring_luniferadoc_xexpression(richstring_luniferadoc_XExpression richstring_luniferadoc_xexpression) {
        this.richstring_luniferadoc_xexpression = richstring_luniferadoc_xexpression;
    }

}