





import java.util.List;
import java.util.ArrayList;

public class HTML_FRAME  {

    private String marginwidth;
    private String marginheight;
    private String scrolling;
    private String name;
    private String noresize;
    private String src;



    public HTML_FRAME(
        String marginwidth,        String marginheight,        String scrolling,        String name,        String noresize,        String src    ) {
        this.marginwidth = marginwidth;
        this.marginheight = marginheight;
        this.scrolling = scrolling;
        this.name = name;
        this.noresize = noresize;
        this.src = src;
    }


    public String getMarginwidth() {
        return marginwidth;
    }

    public void setMarginwidth(String marginwidth) {
        this.marginwidth = marginwidth;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNoresize() {
        return noresize;
    }

    public void setNoresize(String noresize) {
        this.noresize = noresize;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }


}