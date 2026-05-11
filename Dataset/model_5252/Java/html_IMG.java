





import java.util.List;
import java.util.ArrayList;

public class html_IMG extends BODYElement {

    private String alt;
    private String usemap;
    private String ismap;
    private String src;
    private String width;
    private String align;
    private String height;
    private String vspace;
    private String border;
    private String hspace;



    public html_IMG(
        String alt,        String usemap,        String ismap,        String src,        String width,        String align,        String height,        String vspace,        String border,        String hspace    ) {
        super(
        );
        this.alt = alt;
        this.usemap = usemap;
        this.ismap = ismap;
        this.src = src;
        this.width = width;
        this.align = align;
        this.height = height;
        this.vspace = vspace;
        this.border = border;
        this.hspace = hspace;
    }


    public String getAlt() {
        return alt;
    }

    public void setAlt(String alt) {
        this.alt = alt;
    }
    public String getUsemap() {
        return usemap;
    }

    public void setUsemap(String usemap) {
        this.usemap = usemap;
    }
    public String getIsmap() {
        return ismap;
    }

    public void setIsmap(String ismap) {
        this.ismap = ismap;
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
    public String getHspace() {
        return hspace;
    }

    public void setHspace(String hspace) {
        this.hspace = hspace;
    }


}