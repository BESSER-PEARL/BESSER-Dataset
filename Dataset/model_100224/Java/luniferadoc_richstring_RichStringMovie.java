





import java.util.List;
import java.util.ArrayList;

public class luniferadoc_richstring_RichStringMovie extends RichStringMarkup {

    private String height;
    private String type;
    private String width;
    private String src;





    private richstring_luniferadoc_XExpression richstring_luniferadoc_xexpression;


    public luniferadoc_richstring_RichStringMovie(
        String height,        String type,        String width,        String src    ) {
        super(
        );
        this.height = height;
        this.type = type;
        this.width = width;
        this.src = src;
    }


    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }

    public richstring_luniferadoc_XExpression getRichstring_luniferadoc_xexpression() {
        return richstring_luniferadoc_xexpression;
    }

    public void setRichstring_luniferadoc_xexpression(richstring_luniferadoc_XExpression richstring_luniferadoc_xexpression) {
        this.richstring_luniferadoc_xexpression = richstring_luniferadoc_xexpression;
    }

}