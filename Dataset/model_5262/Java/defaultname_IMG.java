





import java.util.List;
import java.util.ArrayList;

public class defaultname_IMG extends BODYElement {

    private String height;
    private String border;
    private String width;
    private String alt;
    private String ismap;
    private String src;
    private String vspace;
    private String usemap;
    private String hspace;
    private String align;



    public defaultname_IMG(
        String height,        String border,        String width,        String alt,        String ismap,        String src,        String vspace,        String usemap,        String hspace,        String align    ) {
        super(
        );
        this.height = height;
        this.border = border;
        this.width = width;
        this.alt = alt;
        this.ismap = ismap;
        this.src = src;
        this.vspace = vspace;
        this.usemap = usemap;
        this.hspace = hspace;
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
    public String getVspace() {
        return vspace;
    }

    public void setVspace(String vspace) {
        this.vspace = vspace;
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
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }


}