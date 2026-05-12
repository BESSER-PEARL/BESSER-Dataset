





import java.util.List;
import java.util.ArrayList;

public class HTML_EMBED extends BODYElement {

    private String width;
    private String hspace;
    private String border;
    private String vspace;
    private String height;
    private String align;
    private String src;



    public HTML_EMBED(
        String width,        String hspace,        String border,        String vspace,        String height,        String align,        String src    ) {
        super(
        );
        this.width = width;
        this.hspace = hspace;
        this.border = border;
        this.vspace = vspace;
        this.height = height;
        this.align = align;
        this.src = src;
    }


    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getHspace() {
        return hspace;
    }

    public void setHspace(String hspace) {
        this.hspace = hspace;
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
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }


}