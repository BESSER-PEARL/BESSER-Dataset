





import java.util.List;
import java.util.ArrayList;

public class Html_IMG extends BODYElement {

    private String hspace;
    private String src;
    private String ismap;
    private String usemap;
    private String align;
    private String border;
    private String vspace;
    private String alt;
    private String width;
    private String height;



    public Html_IMG(
        String hspace,        String src,        String ismap,        String usemap,        String align,        String border,        String vspace,        String alt,        String width,        String height    ) {
        super(
        );
        this.hspace = hspace;
        this.src = src;
        this.ismap = ismap;
        this.usemap = usemap;
        this.align = align;
        this.border = border;
        this.vspace = vspace;
        this.alt = alt;
        this.width = width;
        this.height = height;
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
    public String getIsmap() {
        return ismap;
    }

    public void setIsmap(String ismap) {
        this.ismap = ismap;
    }
    public String getUsemap() {
        return usemap;
    }

    public void setUsemap(String usemap) {
        this.usemap = usemap;
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
    public String getAlt() {
        return alt;
    }

    public void setAlt(String alt) {
        this.alt = alt;
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


}