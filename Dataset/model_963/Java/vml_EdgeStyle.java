





import java.util.List;
import java.util.ArrayList;

public class vml_EdgeStyle extends GraphStyle {

    private int lineWidth;
    private String lineStyle;
    private boolean directed;
    private float weight;



    public vml_EdgeStyle(
        int lineWidth,        String lineStyle,        boolean directed,        float weight    ) {
        super(
        );
        this.lineWidth = lineWidth;
        this.lineStyle = lineStyle;
        this.directed = directed;
        this.weight = weight;
    }


    public int getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(int lineWidth) {
        this.lineWidth = lineWidth;
    }
    public String getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(String lineStyle) {
        this.lineStyle = lineStyle;
    }
    public boolean getDirected() {
        return directed;
    }

    public void setDirected(boolean directed) {
        this.directed = directed;
    }
    public float getWeight() {
        return weight;
    }

    public void setWeight(float weight) {
        this.weight = weight;
    }


}