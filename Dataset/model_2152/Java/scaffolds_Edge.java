





import java.util.List;
import java.util.ArrayList;

public class scaffolds_Edge  {

    private int distance;
    private int weight;





    private scaffolds_ScaffoldGraph scaffolds_scaffoldgraph;


    public scaffolds_Edge(
        int distance,        int weight    ) {
        this.distance = distance;
        this.weight = weight;
    }


    public int getDistance() {
        return distance;
    }

    public void setDistance(int distance) {
        this.distance = distance;
    }
    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public scaffolds_ScaffoldGraph getScaffolds_scaffoldgraph() {
        return scaffolds_scaffoldgraph;
    }

    public void setScaffolds_scaffoldgraph(scaffolds_ScaffoldGraph scaffolds_scaffoldgraph) {
        this.scaffolds_scaffoldgraph = scaffolds_scaffoldgraph;
    }

}