





import java.util.List;
import java.util.ArrayList;

public class HTML_IMG extends BODYElement {

    private String hspace;
    private String usemap;
    private String src;
    private String ismap;
    private String alt;
    private String width;
    private String vspace;
    private String align;
    private String height;
    private String border;



    public HTML_IMG(
        String hspace,        String usemap,        String src,        String ismap,        String alt,        String width,        String vspace,        String align,        String height,        String border    ) {
        super(
        );
        this.hspace = hspace;
        this.usemap = usemap;
        this.src = src;
        this.ismap = ismap;
        this.alt = alt;
        this.width = width;
        this.vspace = vspace;
        this.align = align;
        this.height = height;
        this.border = border;
    }


    public String getHspace() {
        return hspace;
    }

    public void setHspace(String hspace) {
        this.hspace = hspace;
    }
    public String getUsemap() {
        return usemap;
    }

    public void setUsemap(String usemap) {
        this.usemap = usemap;
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


}