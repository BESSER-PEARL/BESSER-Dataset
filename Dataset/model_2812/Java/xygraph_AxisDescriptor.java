





import java.util.List;
import java.util.ArrayList;

public class xygraph_AxisDescriptor  {

    private float rangeLower;
    private float rangeUpper;
    private boolean primarySide;
    private String formatPattern;
    private boolean showMajorGrid;
    private float autoScaleThreshold;
    private String title;
    private String zoomType;
    private boolean autoScale;
    private boolean minorTicksVisible;
    private boolean logScale;
    private boolean autoFormat;
    private boolean showMinorGrid;
    private boolean dateEnabled;
    private String orientation;
    private boolean dashGridLine;





    private xygraph_ColorDescriptor xygraph_colordescriptor;




    private xygraph_ColorDescriptor xygraph_colordescriptor;




    private xygraph_ColorDescriptor xygraph_colordescriptor;




    private xygraph_XYGraphDescriptor xygraph_xygraphdescriptor;




    private xygraph_ColorDescriptor xygraph_colordescriptor;


    public xygraph_AxisDescriptor(
        float rangeLower,        float rangeUpper,        boolean primarySide,        String formatPattern,        boolean showMajorGrid,        float autoScaleThreshold,        String title,        String zoomType,        boolean autoScale,        boolean minorTicksVisible,        boolean logScale,        boolean autoFormat,        boolean showMinorGrid,        boolean dateEnabled,        String orientation,        boolean dashGridLine    ) {
        this.rangeLower = rangeLower;
        this.rangeUpper = rangeUpper;
        this.primarySide = primarySide;
        this.formatPattern = formatPattern;
        this.showMajorGrid = showMajorGrid;
        this.autoScaleThreshold = autoScaleThreshold;
        this.title = title;
        this.zoomType = zoomType;
        this.autoScale = autoScale;
        this.minorTicksVisible = minorTicksVisible;
        this.logScale = logScale;
        this.autoFormat = autoFormat;
        this.showMinorGrid = showMinorGrid;
        this.dateEnabled = dateEnabled;
        this.orientation = orientation;
        this.dashGridLine = dashGridLine;
    }


    public float getRangelower() {
        return rangeLower;
    }

    public void setRangelower(float rangeLower) {
        this.rangeLower = rangeLower;
    }
    public float getRangeupper() {
        return rangeUpper;
    }

    public void setRangeupper(float rangeUpper) {
        this.rangeUpper = rangeUpper;
    }
    public boolean getPrimaryside() {
        return primarySide;
    }

    public void setPrimaryside(boolean primarySide) {
        this.primarySide = primarySide;
    }
    public String getFormatpattern() {
        return formatPattern;
    }

    public void setFormatpattern(String formatPattern) {
        this.formatPattern = formatPattern;
    }
    public boolean getShowmajorgrid() {
        return showMajorGrid;
    }

    public void setShowmajorgrid(boolean showMajorGrid) {
        this.showMajorGrid = showMajorGrid;
    }
    public float getAutoscalethreshold() {
        return autoScaleThreshold;
    }

    public void setAutoscalethreshold(float autoScaleThreshold) {
        this.autoScaleThreshold = autoScaleThreshold;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getZoomtype() {
        return zoomType;
    }

    public void setZoomtype(String zoomType) {
        this.zoomType = zoomType;
    }
    public boolean getAutoscale() {
        return autoScale;
    }

    public void setAutoscale(boolean autoScale) {
        this.autoScale = autoScale;
    }
    public boolean getMinorticksvisible() {
        return minorTicksVisible;
    }

    public void setMinorticksvisible(boolean minorTicksVisible) {
        this.minorTicksVisible = minorTicksVisible;
    }
    public boolean getLogscale() {
        return logScale;
    }

    public void setLogscale(boolean logScale) {
        this.logScale = logScale;
    }
    public boolean getAutoformat() {
        return autoFormat;
    }

    public void setAutoformat(boolean autoFormat) {
        this.autoFormat = autoFormat;
    }
    public boolean getShowminorgrid() {
        return showMinorGrid;
    }

    public void setShowminorgrid(boolean showMinorGrid) {
        this.showMinorGrid = showMinorGrid;
    }
    public boolean getDateenabled() {
        return dateEnabled;
    }

    public void setDateenabled(boolean dateEnabled) {
        this.dateEnabled = dateEnabled;
    }
    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }
    public boolean getDashgridline() {
        return dashGridLine;
    }

    public void setDashgridline(boolean dashGridLine) {
        this.dashGridLine = dashGridLine;
    }

    public xygraph_ColorDescriptor getXygraph_colordescriptor() {
        return xygraph_colordescriptor;
    }

    public void setXygraph_colordescriptor(xygraph_ColorDescriptor xygraph_colordescriptor) {
        this.xygraph_colordescriptor = xygraph_colordescriptor;
    }
    public xygraph_ColorDescriptor getXygraph_colordescriptor() {
        return xygraph_colordescriptor;
    }

    public void setXygraph_colordescriptor(xygraph_ColorDescriptor xygraph_colordescriptor) {
        this.xygraph_colordescriptor = xygraph_colordescriptor;
    }
    public xygraph_ColorDescriptor getXygraph_colordescriptor() {
        return xygraph_colordescriptor;
    }

    public void setXygraph_colordescriptor(xygraph_ColorDescriptor xygraph_colordescriptor) {
        this.xygraph_colordescriptor = xygraph_colordescriptor;
    }
    public xygraph_XYGraphDescriptor getXygraph_xygraphdescriptor() {
        return xygraph_xygraphdescriptor;
    }

    public void setXygraph_xygraphdescriptor(xygraph_XYGraphDescriptor xygraph_xygraphdescriptor) {
        this.xygraph_xygraphdescriptor = xygraph_xygraphdescriptor;
    }
    public xygraph_ColorDescriptor getXygraph_colordescriptor() {
        return xygraph_colordescriptor;
    }

    public void setXygraph_colordescriptor(xygraph_ColorDescriptor xygraph_colordescriptor) {
        this.xygraph_colordescriptor = xygraph_colordescriptor;
    }

}