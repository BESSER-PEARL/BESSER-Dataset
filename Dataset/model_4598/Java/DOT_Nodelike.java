





import java.util.List;
import java.util.ArrayList;

public class DOT_Nodelike extends GraphElement {






    private DOT_Layer dot_layer;




    private DOT_Graph dot_graph;




    private List<DOT_Layer> dot_layers;




    private DOT_Graph dot_graph;


    public DOT_Nodelike(
    ) {
        super(
        );
        this.dot_layers = new ArrayList<>();
    }

    public DOT_Nodelike(
        ArrayList<DOT_Layer> dot_layers    ) {
        this.dot_layers = dot_layers;
    }


    public DOT_Layer getDot_layer() {
        return dot_layer;
    }

    public void setDot_layer(DOT_Layer dot_layer) {
        this.dot_layer = dot_layer;
    }
    public DOT_Graph getDot_graph() {
        return dot_graph;
    }

    public void setDot_graph(DOT_Graph dot_graph) {
        this.dot_graph = dot_graph;
    }
    public List<DOT_Layer> getDot_layers() {
        return dot_layers;
    }

    public void addDot_layer(Dot_layer dot_layer) {
        this.dot_layers.add(dot_layer);
    }
    public DOT_Graph getDot_graph() {
        return dot_graph;
    }

    public void setDot_graph(DOT_Graph dot_graph) {
        this.dot_graph = dot_graph;
    }

}