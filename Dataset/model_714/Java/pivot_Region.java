





import java.util.List;
import java.util.ArrayList;

public class pivot_Region extends Namespace {






    private pivot_Region pivot_region;




    private pivot_Vertex pivot_vertex;




    private List<pivot_Vertex> pivot_vertexs;


    public pivot_Region(
    ) {
        super(
        );
        this.pivot_vertexs = new ArrayList<>();
    }

    public pivot_Region(
        ArrayList<pivot_Vertex> pivot_vertexs    ) {
        this.pivot_vertexs = pivot_vertexs;
    }


    public pivot_Region getPivot_region() {
        return pivot_region;
    }

    public void setPivot_region(pivot_Region pivot_region) {
        this.pivot_region = pivot_region;
    }
    public pivot_Vertex getPivot_vertex() {
        return pivot_vertex;
    }

    public void setPivot_vertex(pivot_Vertex pivot_vertex) {
        this.pivot_vertex = pivot_vertex;
    }
    public List<pivot_Vertex> getPivot_vertexs() {
        return pivot_vertexs;
    }

    public void addPivot_vertex(Pivot_vertex pivot_vertex) {
        this.pivot_vertexs.add(pivot_vertex);
    }

}