





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Canvas extends Identity {






    private List<gmfgraph_Node> gmfgraph_nodes;




    private List<gmfgraph_FigureGallery> gmfgraph_figuregallerys;


    public gmfgraph_Canvas(
    ) {
        super(
        );
        this.gmfgraph_nodes = new ArrayList<>();
        this.gmfgraph_figuregallerys = new ArrayList<>();
    }

    public gmfgraph_Canvas(
        ArrayList<gmfgraph_Node> gmfgraph_nodes,        ArrayList<gmfgraph_FigureGallery> gmfgraph_figuregallerys    ) {
        this.gmfgraph_nodes = gmfgraph_nodes;
        this.gmfgraph_figuregallerys = gmfgraph_figuregallerys;
    }


    public List<gmfgraph_Node> getGmfgraph_nodes() {
        return gmfgraph_nodes;
    }

    public void addGmfgraph_node(Gmfgraph_node gmfgraph_node) {
        this.gmfgraph_nodes.add(gmfgraph_node);
    }
    public List<gmfgraph_FigureGallery> getGmfgraph_figuregallerys() {
        return gmfgraph_figuregallerys;
    }

    public void addGmfgraph_figuregallery(Gmfgraph_figuregallery gmfgraph_figuregallery) {
        this.gmfgraph_figuregallerys.add(gmfgraph_figuregallery);
    }

}