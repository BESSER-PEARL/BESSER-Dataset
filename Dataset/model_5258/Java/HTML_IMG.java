





import java.util.List;
import java.util.ArrayList;

public class HTML_IMG extends BODYElement {

    private String ismap;
    private String usemap;
    private String hspace;
    private String border;
    private String alt;
    private String align;
    private String src;
    private String width;
    private String height;
    private String vspace;



    public HTML_IMG(
        String ismap,        String usemap,        String hspace,        String border,        String alt,        String align,        String src,        String width,        String height,        String vspace    ) {
        super(
        );
        this.ismap = ismap;
        this.usemap = usemap;
        this.hspace = hspace;
        this.border = border;
        this.alt = alt;
        this.align = align;
        this.src = src;
        this.width = width;
        this.height = height;
        this.vspace = vspace;
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
    public String getAlt() {
        return alt;
    }

    public void setAlt(String alt) {
        this.alt = alt;
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
    public String getVspace() {
        return vspace;
    }

    public void setVspace(String vspace) {
        this.vspace = vspace;
    }


}