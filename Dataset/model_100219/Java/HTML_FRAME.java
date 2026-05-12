





import java.util.List;
import java.util.ArrayList;

public class HTML_FRAME  {

    private String name;
    private String src;
    private String noresize;
    private String marginheight;
    private String scrolling;
    private String marginwidth;



    public HTML_FRAME(
        String name,        String src,        String noresize,        String marginheight,        String scrolling,        String marginwidth    ) {
        this.name = name;
        this.src = src;
        this.noresize = noresize;
        this.marginheight = marginheight;
        this.scrolling = scrolling;
        this.marginwidth = marginwidth;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getNoresize() {
        return noresize;
    }

    public void setNoresize(String noresize) {
        this.noresize = noresize;
    }
    public String getMarginheight() {
        return marginheight;
    }

    public void setMarginheight(String marginheight) {
        this.marginheight = marginheight;
    }
    public String getScrolling() {
        return scrolling;
    }

    public void setScrolling(String scrolling) {
        this.scrolling = scrolling;
    }
    public String getMarginwidth() {
        return marginwidth;
    }

    public void setMarginwidth(String marginwidth) {
        this.marginwidth = marginwidth;
    }


}