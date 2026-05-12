





import java.util.List;
import java.util.ArrayList;

public class html_EMBED extends BODYElement {

    private String hspace;
    private String height;
    private String src;
    private String align;
    private String width;
    private String vspace;
    private String border;



    public html_EMBED(
        String hspace,        String height,        String src,        String align,        String width,        String vspace,        String border    ) {
        super(
        );
        this.hspace = hspace;
        this.height = height;
        this.src = src;
        this.align = align;
        this.width = width;
        this.vspace = vspace;
        this.border = border;
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
    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }


}