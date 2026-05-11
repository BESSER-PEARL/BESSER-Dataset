





import java.util.List;
import java.util.ArrayList;

public class html_IMG extends BODYElement {

    private String align;
    private String vspace;
    private String ismap;
    private String border;
    private String src;
    private String width;
    private String alt;
    private String height;
    private String usemap;
    private String hspace;



    public html_IMG(
        String align,        String vspace,        String ismap,        String border,        String src,        String width,        String alt,        String height,        String usemap,        String hspace    ) {
        super(
        );
        this.align = align;
        this.vspace = vspace;
        this.ismap = ismap;
        this.border = border;
        this.src = src;
        this.width = width;
        this.alt = alt;
        this.height = height;
        this.usemap = usemap;
        this.hspace = hspace;
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
    public String getIsmap() {
        return ismap;
    }

    public void setIsmap(String ismap) {
        this.ismap = ismap;
    }
    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
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
    public String getAlt() {
        return alt;
    }

    public void setAlt(String alt) {
        this.alt = alt;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
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


}