





import java.util.List;
import java.util.ArrayList;

public class ZestGraph_GraphNode extends GraphItem {

    private float width;
    private String backColor;
    private float height;
    private String nodeStyle;
    private String shape;





    private ZestGraph_GraphContainer zestgraph_graphcontainer;


    public ZestGraph_GraphNode(
        float width,        String backColor,        float height,        String nodeStyle,        String shape    ) {
        super(
        );
        this.width = width;
        this.backColor = backColor;
        this.height = height;
        this.nodeStyle = nodeStyle;
        this.shape = shape;
    }


    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }
    public String getBackcolor() {
        return backColor;
    }

    public void setBackcolor(String backColor) {
        this.backColor = backColor;
    }
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public String getNodestyle() {
        return nodeStyle;
    }

    public void setNodestyle(String nodeStyle) {
        this.nodeStyle = nodeStyle;
    }
    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }

    public ZestGraph_GraphContainer getZestgraph_graphcontainer() {
        return zestgraph_graphcontainer;
    }

    public void setZestgraph_graphcontainer(ZestGraph_GraphContainer zestgraph_graphcontainer) {
        this.zestgraph_graphcontainer = zestgraph_graphcontainer;
    }

}