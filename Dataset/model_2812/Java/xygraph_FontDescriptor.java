





import java.util.List;
import java.util.ArrayList;

public class xygraph_FontDescriptor  {

    private int size;
    private int style;
    private String name;





    private xygraph_XYGraphDescriptor xygraph_xygraphdescriptor;




    private xygraph_AxisDescriptor xygraph_axisdescriptor;




    private xygraph_AxisDescriptor xygraph_axisdescriptor;


    public xygraph_FontDescriptor(
        int size,        int style,        String name    ) {
        this.size = size;
        this.style = style;
        this.name = name;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public int getStyle() {
        return style;
    }

    public void setStyle(int style) {
        this.style = style;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public xygraph_XYGraphDescriptor getXygraph_xygraphdescriptor() {
        return xygraph_xygraphdescriptor;
    }

    public void setXygraph_xygraphdescriptor(xygraph_XYGraphDescriptor xygraph_xygraphdescriptor) {
        this.xygraph_xygraphdescriptor = xygraph_xygraphdescriptor;
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

}