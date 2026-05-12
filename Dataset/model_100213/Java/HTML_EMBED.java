





import java.util.List;
import java.util.ArrayList;

public class HTML_EMBED extends BODYElement {

    private String width;
    private String align;
    private String border;
    private String vspace;
    private String hspace;
    private String height;
    private String src;



    public HTML_EMBED(
        String width,        String align,        String border,        String vspace,        String hspace,        String height,        String src    ) {
        super(
        );
        this.width = width;
        this.align = align;
        this.border = border;
        this.vspace = vspace;
        this.hspace = hspace;
        this.height = height;
        this.src = src;
    }


    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }
    public String getVspace() {
        return vspace;
    }

    public void setVspace(String vspace) {
        this.vspace = vspace;
    }
    public String getHspace() {
        return hspace;
    }

    public void setHspace(String hspace) {
        this.hspace = hspace;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }


}