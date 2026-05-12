





import java.util.List;
import java.util.ArrayList;

public class HTML_EMBED extends BODYElement {

    private String hspace;
    private String height;
    private String border;
    private String align;
    private String width;
    private String vspace;
    private String src;



    public HTML_EMBED(
        String hspace,        String height,        String border,        String align,        String width,        String vspace,        String src    ) {
        super(
        );
        this.hspace = hspace;
        this.height = height;
        this.border = border;
        this.align = align;
        this.width = width;
        this.vspace = vspace;
        this.src = src;
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
    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
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
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }


}