





import java.util.List;
import java.util.ArrayList;

public class HTML_FRAME  {

    private String noresize;
    private String name;
    private String scrolling;
    private String marginheight;
    private String src;
    private String marginwidth;



    public HTML_FRAME(
        String noresize,        String name,        String scrolling,        String marginheight,        String src,        String marginwidth    ) {
        this.noresize = noresize;
        this.name = name;
        this.scrolling = scrolling;
        this.marginheight = marginheight;
        this.src = src;
        this.marginwidth = marginwidth;
    }


    public String getNoresize() {
        return noresize;
    }

    public void setNoresize(String noresize) {
        this.noresize = noresize;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getScrolling() {
        return scrolling;
    }

    public void setScrolling(String scrolling) {
        this.scrolling = scrolling;
    }
    public String getMarginheight() {
        return marginheight;
    }

    public void setMarginheight(String marginheight) {
        this.marginheight = marginheight;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getMarginwidth() {
        return marginwidth;
    }

    public void setMarginwidth(String marginwidth) {
        this.marginwidth = marginwidth;
    }


}