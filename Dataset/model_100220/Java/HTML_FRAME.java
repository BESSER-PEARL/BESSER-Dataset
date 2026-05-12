





import java.util.List;
import java.util.ArrayList;

public class HTML_FRAME  {

    private String marginheight;
    private String scrolling;
    private String src;
    private String name;
    private String marginwidth;
    private String noresize;



    public HTML_FRAME(
        String marginheight,        String scrolling,        String src,        String name,        String marginwidth,        String noresize    ) {
        this.marginheight = marginheight;
        this.scrolling = scrolling;
        this.src = src;
        this.name = name;
        this.marginwidth = marginwidth;
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
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMarginwidth() {
        return marginwidth;
    }

    public void setMarginwidth(String marginwidth) {
        this.marginwidth = marginwidth;
    }
    public String getNoresize() {
        return noresize;
    }

    public void setNoresize(String noresize) {
        this.noresize = noresize;
    }


}