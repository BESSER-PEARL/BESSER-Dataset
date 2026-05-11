





import java.util.List;
import java.util.ArrayList;

public class html_IMG extends BODYElement {

    private String border;
    private String vspace;
    private String height;
    private String alt;
    private String ismap;
    private String src;
    private String hspace;
    private String usemap;
    private String width;
    private String align;



    public html_IMG(
        String border,        String vspace,        String height,        String alt,        String ismap,        String src,        String hspace,        String usemap,        String width,        String align    ) {
        super(
        );
        this.border = border;
        this.vspace = vspace;
        this.height = height;
        this.alt = alt;
        this.ismap = ismap;
        this.src = src;
        this.hspace = hspace;
        this.usemap = usemap;
        this.width = width;
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
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
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
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
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


}