





import java.util.List;
import java.util.ArrayList;

public class scaffolds_Vertex  {

    private int num;





    private scaffolds_Contig scaffolds_contig;




    private scaffolds_Edge scaffolds_edge;




    private List<scaffolds_Edge> scaffolds_edges;


    public scaffolds_Vertex(
        int num    ) {
        this.num = num;
        this.scaffolds_edges = new ArrayList<>();
    }

    public scaffolds_Vertex(
        int num        ArrayList<scaffolds_Edge> scaffolds_edges    ) {
        this.num = num;
        this.scaffolds_edges = scaffolds_edges;
    }

    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }

    public scaffolds_Contig getScaffolds_contig() {
        return scaffolds_contig;
    }

    public void setScaffolds_contig(scaffolds_Contig scaffolds_contig) {
        this.scaffolds_contig = scaffolds_contig;
    }
    public scaffolds_Edge getScaffolds_edge() {
        return scaffolds_edge;
    }

    public void setScaffolds_edge(scaffolds_Edge scaffolds_edge) {
        this.scaffolds_edge = scaffolds_edge;
    }
    public List<scaffolds_Edge> getScaffolds_edges() {
        return scaffolds_edges;
    }

    public void addScaffolds_edge(Scaffolds_edge scaffolds_edge) {
        this.scaffolds_edges.add(scaffolds_edge);
    }

}