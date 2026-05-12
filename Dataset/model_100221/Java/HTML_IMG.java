





import java.util.List;
import java.util.ArrayList;

public class HTML_IMG extends BODYElement {

    private String usemap;
    private String hspace;
    private String height;
    private String border;
    private String ismap;
    private String width;
    private String align;
    private String vspace;
    private String alt;
    private String src;



    public HTML_IMG(
        String usemap,        String hspace,        String height,        String border,        String ismap,        String width,        String align,        String vspace,        String alt,        String src    ) {
        super(
        );
        this.usemap = usemap;
        this.hspace = hspace;
        this.height = height;
        this.border = border;
        this.ismap = ismap;
        this.width = width;
        this.align = align;
        this.vspace = vspace;
        this.alt = alt;
        this.src = src;
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
    public String getIsmap() {
        return ismap;
    }

    public void setIsmap(String ismap) {
        this.ismap = ismap;
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
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }


}