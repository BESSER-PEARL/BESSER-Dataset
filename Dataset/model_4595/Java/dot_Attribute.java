





import java.util.List;
import java.util.ArrayList;

public class dot_Attribute  {

    private int weight;





    private dot_DirectedEdge dot_directededge;




    private dot_UnDirectedEdge dot_undirectededge;


    public dot_Attribute(
        int weight    ) {
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public dot_DirectedEdge getDot_directededge() {
        return dot_directededge;
    }

    public void setDot_directededge(dot_DirectedEdge dot_directededge) {
        this.dot_directededge = dot_directededge;
    }
    public dot_UnDirectedEdge getDot_undirectededge() {
        return dot_undirectededge;
    }

    public void setDot_undirectededge(dot_UnDirectedEdge dot_undirectededge) {
        this.dot_undirectededge = dot_undirectededge;
    }

}