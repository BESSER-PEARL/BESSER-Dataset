





import java.util.List;
import java.util.ArrayList;

public class xygraph_XYGraphDescriptor  {

    private String zoomType;
    private boolean showTitle;
    private boolean showLegend;
    private boolean transparent;
    private String title;
    private boolean showPlotAreaBorder;



    public xygraph_XYGraphDescriptor(
        String zoomType,        boolean showTitle,        boolean showLegend,        boolean transparent,        String title,        boolean showPlotAreaBorder    ) {
        this.zoomType = zoomType;
        this.showTitle = showTitle;
        this.showLegend = showLegend;
        this.transparent = transparent;
        this.title = title;
        this.showPlotAreaBorder = showPlotAreaBorder;
    }


    public String getZoomtype() {
        return zoomType;
    }

    public void setZoomtype(String zoomType) {
        this.zoomType = zoomType;
    }
    public boolean getShowtitle() {
        return showTitle;
    }

    public void setShowtitle(boolean showTitle) {
        this.showTitle = showTitle;
    }
    public boolean getShowlegend() {
        return showLegend;
    }

    public void setShowlegend(boolean showLegend) {
        this.showLegend = showLegend;
    }
    public boolean getTransparent() {
        return transparent;
    }

    public void setTransparent(boolean transparent) {
        this.transparent = transparent;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public boolean getShowplotareaborder() {
        return showPlotAreaBorder;
    }

    public void setShowplotareaborder(boolean showPlotAreaBorder) {
        this.showPlotAreaBorder = showPlotAreaBorder;
    }


}