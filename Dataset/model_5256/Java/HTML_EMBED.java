





import java.util.List;
import java.util.ArrayList;

public class HTML_EMBED extends BODYElement {

    private String src;
    private String border;
    private String width;
    private String vspace;
    private String align;
    private String hspace;
    private String height;



    public HTML_EMBED(
        String src,        String border,        String width,        String vspace,        String align,        String hspace,        String height    ) {
        super(
        );
        this.src = src;
        this.border = border;
        this.width = width;
        this.vspace = vspace;
        this.align = align;
        this.hspace = hspace;
        this.height = height;
    }


    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getVspace() {
        return vspace;
    }

    public void setVspace(String vspace) {
        this.vspace = vspace;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
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


}