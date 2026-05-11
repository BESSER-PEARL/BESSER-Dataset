





import java.util.List;
import java.util.ArrayList;

public class xygraph_TraceDescriptor  {

    private String baseLine;
    private int lineWidth;
    private boolean antiAliasing;
    private boolean drawYErrorInArea;
    private String pointStyle;
    private int errorBarCapWidth;
    private String name;
    private String yErrorBarType;
    private boolean errorBarEnabled;
    private String xErrorBarType;
    private int areaAlpha;
    private int pointSize;
    private String traceType;





    private xygraph_XYGraphDescriptor xygraph_xygraphdescriptor;




    private xygraph_ColorDescriptor xygraph_colordescriptor;




    private xygraph_AxisDescriptor xygraph_axisdescriptor;




    private xygraph_AxisDescriptor xygraph_axisdescriptor;




    private xygraph_ColorDescriptor xygraph_colordescriptor;




    private xygraph_XYGraphDescriptor xygraph_xygraphdescriptor;


    public xygraph_TraceDescriptor(
        String baseLine,        int lineWidth,        boolean antiAliasing,        boolean drawYErrorInArea,        String pointStyle,        int errorBarCapWidth,        String name,        String yErrorBarType,        boolean errorBarEnabled,        String xErrorBarType,        int areaAlpha,        int pointSize,        String traceType    ) {
        this.baseLine = baseLine;
        this.lineWidth = lineWidth;
        this.antiAliasing = antiAliasing;
        this.drawYErrorInArea = drawYErrorInArea;
        this.pointStyle = pointStyle;
        this.errorBarCapWidth = errorBarCapWidth;
        this.name = name;
        this.yErrorBarType = yErrorBarType;
        this.errorBarEnabled = errorBarEnabled;
        this.xErrorBarType = xErrorBarType;
        this.areaAlpha = areaAlpha;
        this.pointSize = pointSize;
        this.traceType = traceType;
    }


    public String getBaseline() {
        return baseLine;
    }

    public void setBaseline(String baseLine) {
        this.baseLine = baseLine;
    }
    public int getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(int lineWidth) {
        this.lineWidth = lineWidth;
    }
    public boolean getAntialiasing() {
        return antiAliasing;
    }

    public void setAntialiasing(boolean antiAliasing) {
        this.antiAliasing = antiAliasing;
    }
    public boolean getDrawyerrorinarea() {
        return drawYErrorInArea;
    }

    public void setDrawyerrorinarea(boolean drawYErrorInArea) {
        this.drawYErrorInArea = drawYErrorInArea;
    }
    public String getPointstyle() {
        return pointStyle;
    }

    public void setPointstyle(String pointStyle) {
        this.pointStyle = pointStyle;
    }
    public int getErrorbarcapwidth() {
        return errorBarCapWidth;
    }

    public void setErrorbarcapwidth(int errorBarCapWidth) {
        this.errorBarCapWidth = errorBarCapWidth;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getYerrorbartype() {
        return yErrorBarType;
    }

    public void setYerrorbartype(String yErrorBarType) {
        this.yErrorBarType = yErrorBarType;
    }
    public boolean getErrorbarenabled() {
        return errorBarEnabled;
    }

    public void setErrorbarenabled(boolean errorBarEnabled) {
        this.errorBarEnabled = errorBarEnabled;
    }
    public String getXerrorbartype() {
        return xErrorBarType;
    }

    public void setXerrorbartype(String xErrorBarType) {
        this.xErrorBarType = xErrorBarType;
    }
    public int getAreaalpha() {
        return areaAlpha;
    }

    public void setAreaalpha(int areaAlpha) {
        this.areaAlpha = areaAlpha;
    }
    public int getPointsize() {
        return pointSize;
    }

    public void setPointsize(int pointSize) {
        this.pointSize = pointSize;
    }
    public String getTracetype() {
        return traceType;
    }

    public void setTracetype(String traceType) {
        this.traceType = traceType;
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
    public xygraph_AxisDescriptor getXygraph_axisdescriptor() {
        return xygraph_axisdescriptor;
    }

    public void setXygraph_axisdescriptor(xygraph_AxisDescriptor xygraph_axisdescriptor) {
        this.xygraph_axisdescriptor = xygraph_axisdescriptor;
    }
    public xygraph_AxisDescriptor getXygraph_axisdescriptor() {
        return xygraph_axisdescriptor;
    }

    public void setXygraph_axisdescriptor(xygraph_AxisDescriptor xygraph_axisdescriptor) {
        this.xygraph_axisdescriptor = xygraph_axisdescriptor;
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

}