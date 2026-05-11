





import java.util.List;
import java.util.ArrayList;

public class di_DocumentRoot  {

    private String mixed;





    private List<di_EStringToStringMapEntry> di_estringtostringmapentrys;




    private List<di_Node> di_nodes;




    private List<di_Connector> di_connectors;




    private List<di_Bendpoint> di_bendpoints;




    private List<di_EStringToStringMapEntry> di_estringtostringmapentrys;




    private List<di_Diagram> di_diagrams;


    public di_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.di_estringtostringmapentrys = new ArrayList<>();
        this.di_nodes = new ArrayList<>();
        this.di_connectors = new ArrayList<>();
        this.di_bendpoints = new ArrayList<>();
        this.di_estringtostringmapentrys = new ArrayList<>();
        this.di_diagrams = new ArrayList<>();
    }

    public di_DocumentRoot(
        String mixed        ArrayList<di_EStringToStringMapEntry> di_estringtostringmapentrys,        ArrayList<di_Node> di_nodes,        ArrayList<di_Connector> di_connectors,        ArrayList<di_Bendpoint> di_bendpoints,        ArrayList<di_EStringToStringMapEntry> di_estringtostringmapentrys,        ArrayList<di_Diagram> di_diagrams    ) {
        this.mixed = mixed;
        this.di_estringtostringmapentrys = di_estringtostringmapentrys;
        this.di_nodes = di_nodes;
        this.di_connectors = di_connectors;
        this.di_bendpoints = di_bendpoints;
        this.di_estringtostringmapentrys = di_estringtostringmapentrys;
        this.di_diagrams = di_diagrams;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<di_EStringToStringMapEntry> getDi_estringtostringmapentrys() {
        return di_estringtostringmapentrys;
    }

    public void addDi_estringtostringmapentry(Di_estringtostringmapentry di_estringtostringmapentry) {
        this.di_estringtostringmapentrys.add(di_estringtostringmapentry);
    }
    public List<di_Node> getDi_nodes() {
        return di_nodes;
    }

    public void addDi_node(Di_node di_node) {
        this.di_nodes.add(di_node);
    }
    public List<di_Connector> getDi_connectors() {
        return di_connectors;
    }

    public void addDi_connector(Di_connector di_connector) {
        this.di_connectors.add(di_connector);
    }
    public List<di_Bendpoint> getDi_bendpoints() {
        return di_bendpoints;
    }

    public void addDi_bendpoint(Di_bendpoint di_bendpoint) {
        this.di_bendpoints.add(di_bendpoint);
    }
    public List<di_EStringToStringMapEntry> getDi_estringtostringmapentrys() {
        return di_estringtostringmapentrys;
    }

    public void addDi_estringtostringmapentry(Di_estringtostringmapentry di_estringtostringmapentry) {
        this.di_estringtostringmapentrys.add(di_estringtostringmapentry);
    }
    public List<di_Diagram> getDi_diagrams() {
        return di_diagrams;
    }

    public void addDi_diagram(Di_diagram di_diagram) {
        this.di_diagrams.add(di_diagram);
    }

}