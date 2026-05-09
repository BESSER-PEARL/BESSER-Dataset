





import java.util.List;
import java.util.ArrayList;

public class ZestGraph_GraphNode extends GraphItem {

    private String shape;
    private float width;
    private String nodeStyle;
    private float height;
    private String backColor;





    private ZestGraph_GraphContainer zestgraph_graphcontainer;


    public ZestGraph_GraphNode(
        String shape,        float width,        String nodeStyle,        float height,        String backColor    ) {
        super(
        );
        this.shape = shape;
        this.width = width;
        this.nodeStyle = nodeStyle;
        this.height = height;
        this.backColor = backColor;
    }


    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }
    public String getNodestyle() {
        return nodeStyle;
    }

    public void setNodestyle(String nodeStyle) {
        this.nodeStyle = nodeStyle;
    }
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public String getBackcolor() {
        return backColor;
    }

    public void setBackcolor(String backColor) {
        this.backColor = backColor;
    }

    public ZestGraph_GraphContainer getZestgraph_graphcontainer() {
        return zestgraph_graphcontainer;
    }

    public void setZestgraph_graphcontainer(ZestGraph_GraphContainer zestgraph_graphcontainer) {
        this.zestgraph_graphcontainer = zestgraph_graphcontainer;
    }

}