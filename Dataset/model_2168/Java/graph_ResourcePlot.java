





import java.util.List;
import java.util.ArrayList;

public class graph_ResourcePlot  {

    private String rgb;
    private String name;
    private float min;
    private String fit;
    private float max;





    private graph_ResourceGraph graph_resourcegraph;


    public graph_ResourcePlot(
        String rgb,        String name,        float min,        String fit,        float max    ) {
        this.rgb = rgb;
        this.name = name;
        this.min = min;
        this.fit = fit;
        this.max = max;
    }


    public String getRgb() {
        return rgb;
    }

    public void setRgb(String rgb) {
        this.rgb = rgb;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getMin() {
        return min;
    }

    public void setMin(float min) {
        this.min = min;
    }
    public String getFit() {
        return fit;
    }

    public void setFit(String fit) {
        this.fit = fit;
    }
    public float getMax() {
        return max;
    }

    public void setMax(float max) {
        this.max = max;
    }

    public graph_ResourceGraph getGraph_resourcegraph() {
        return graph_resourcegraph;
    }

    public void setGraph_resourcegraph(graph_ResourceGraph graph_resourcegraph) {
        this.graph_resourcegraph = graph_resourcegraph;
    }

}