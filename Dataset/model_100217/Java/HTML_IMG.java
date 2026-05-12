





import java.util.List;
import java.util.ArrayList;

public class HTML_IMG extends BODYElement {

    private String vspace;
    private String alt;
    private String ismap;
    private String usemap;
    private String width;
    private String border;
    private String height;
    private String src;
    private String align;
    private String hspace;



    public HTML_IMG(
        String vspace,        String alt,        String ismap,        String usemap,        String width,        String border,        String height,        String src,        String align,        String hspace    ) {
        super(
        );
        this.vspace = vspace;
        this.alt = alt;
        this.ismap = ismap;
        this.usemap = usemap;
        this.width = width;
        this.border = border;
        this.height = height;
        this.src = src;
        this.align = align;
        this.hspace = hspace;
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
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
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
    public String getHspace() {
        return hspace;
    }

    public void setHspace(String hspace) {
        this.hspace = hspace;
    }


}