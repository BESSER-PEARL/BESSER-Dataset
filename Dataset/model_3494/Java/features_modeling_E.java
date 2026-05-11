





import java.util.List;
import java.util.ArrayList;

public class features_modeling_E  {






    private List<features_modeling_Edge> features_modeling_edges;


    public features_modeling_E(
    ) {
        this.features_modeling_edges = new ArrayList<>();
    }

    public features_modeling_E(
        ArrayList<features_modeling_Edge> features_modeling_edges    ) {
        this.features_modeling_edges = features_modeling_edges;
    }


    public List<features_modeling_Edge> getFeatures_modeling_edges() {
        return features_modeling_edges;
    }

    public void addFeatures_modeling_edge(Features_modeling_edge features_modeling_edge) {
        this.features_modeling_edges.add(features_modeling_edge);
    }

}