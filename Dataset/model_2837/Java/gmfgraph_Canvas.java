





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Canvas extends Identity {






    private List<gmfgraph_DiagramLabel> gmfgraph_diagramlabels;




    private List<gmfgraph_Compartment> gmfgraph_compartments;


    public gmfgraph_Canvas(
    ) {
        super(
        );
        this.gmfgraph_diagramlabels = new ArrayList<>();
        this.gmfgraph_compartments = new ArrayList<>();
    }

    public gmfgraph_Canvas(
        ArrayList<gmfgraph_DiagramLabel> gmfgraph_diagramlabels,        ArrayList<gmfgraph_Compartment> gmfgraph_compartments    ) {
        this.gmfgraph_diagramlabels = gmfgraph_diagramlabels;
        this.gmfgraph_compartments = gmfgraph_compartments;
    }


    public List<gmfgraph_DiagramLabel> getGmfgraph_diagramlabels() {
        return gmfgraph_diagramlabels;
    }

    public void addGmfgraph_diagramlabel(Gmfgraph_diagramlabel gmfgraph_diagramlabel) {
        this.gmfgraph_diagramlabels.add(gmfgraph_diagramlabel);
    }
    public List<gmfgraph_Compartment> getGmfgraph_compartments() {
        return gmfgraph_compartments;
    }

    public void addGmfgraph_compartment(Gmfgraph_compartment gmfgraph_compartment) {
        this.gmfgraph_compartments.add(gmfgraph_compartment);
    }

}