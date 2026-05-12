





import java.util.List;
import java.util.ArrayList;

public class HTML_EMBED extends BODYElement {

    private String height;
    private String align;
    private String vspace;
    private String width;
    private String hspace;
    private String src;
    private String border;



    public HTML_EMBED(
        String height,        String align,        String vspace,        String width,        String hspace,        String src,        String border    ) {
        super(
        );
        this.height = height;
        this.align = align;
        this.vspace = vspace;
        this.width = width;
        this.hspace = hspace;
        this.src = src;
        this.border = border;
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
    public String getVspace() {
        return vspace;
    }

    public void setVspace(String vspace) {
        this.vspace = vspace;
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


}