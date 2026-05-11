





import java.util.List;
import java.util.ArrayList;

public class defaultname_FRAME  {

    private String name;
    private String scrolling;
    private String src;
    private String noresize;
    private String marginwidth;
    private String marginheight;



    public defaultname_FRAME(
        String name,        String scrolling,        String src,        String noresize,        String marginwidth,        String marginheight    ) {
        this.name = name;
        this.scrolling = scrolling;
        this.src = src;
        this.noresize = noresize;
        this.marginwidth = marginwidth;
        this.marginheight = marginheight;
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


}