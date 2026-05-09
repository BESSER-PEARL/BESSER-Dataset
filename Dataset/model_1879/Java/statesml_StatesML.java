





import java.util.List;
import java.util.ArrayList;

public class statesml_StatesML  {






    private List<statesml_DataTypeLibrary> statesml_datatypelibrarys;




    private List<statesml_Edge> statesml_edges;




    private List<statesml_SystemUnitLibrariy> statesml_systemunitlibrariys;




    private List<statesml_Event> statesml_events;




    private List<statesml_Node> statesml_nodes;




    private List<statesml_SystemUnits> statesml_systemunitss;




    private List<statesml_Attribute> statesml_attributes;


    public statesml_StatesML(
    ) {
        this.statesml_datatypelibrarys = new ArrayList<>();
        this.statesml_edges = new ArrayList<>();
        this.statesml_systemunitlibrariys = new ArrayList<>();
        this.statesml_events = new ArrayList<>();
        this.statesml_nodes = new ArrayList<>();
        this.statesml_systemunitss = new ArrayList<>();
        this.statesml_attributes = new ArrayList<>();
    }

    public statesml_StatesML(
        ArrayList<statesml_DataTypeLibrary> statesml_datatypelibrarys,        ArrayList<statesml_Edge> statesml_edges,        ArrayList<statesml_SystemUnitLibrariy> statesml_systemunitlibrariys,        ArrayList<statesml_Event> statesml_events,        ArrayList<statesml_Node> statesml_nodes,        ArrayList<statesml_SystemUnits> statesml_systemunitss,        ArrayList<statesml_Attribute> statesml_attributes    ) {
        this.statesml_datatypelibrarys = statesml_datatypelibrarys;
        this.statesml_edges = statesml_edges;
        this.statesml_systemunitlibrariys = statesml_systemunitlibrariys;
        this.statesml_events = statesml_events;
        this.statesml_nodes = statesml_nodes;
        this.statesml_systemunitss = statesml_systemunitss;
        this.statesml_attributes = statesml_attributes;
    }


    public List<statesml_DataTypeLibrary> getStatesml_datatypelibrarys() {
        return statesml_datatypelibrarys;
    }

    public void addStatesml_datatypelibrary(Statesml_datatypelibrary statesml_datatypelibrary) {
        this.statesml_datatypelibrarys.add(statesml_datatypelibrary);
    }
    public List<statesml_Edge> getStatesml_edges() {
        return statesml_edges;
    }

    public void addStatesml_edge(Statesml_edge statesml_edge) {
        this.statesml_edges.add(statesml_edge);
    }
    public List<statesml_SystemUnitLibrariy> getStatesml_systemunitlibrariys() {
        return statesml_systemunitlibrariys;
    }

    public void addStatesml_systemunitlibrariy(Statesml_systemunitlibrariy statesml_systemunitlibrariy) {
        this.statesml_systemunitlibrariys.add(statesml_systemunitlibrariy);
    }
    public List<statesml_Event> getStatesml_events() {
        return statesml_events;
    }

    public void addStatesml_event(Statesml_event statesml_event) {
        this.statesml_events.add(statesml_event);
    }
    public List<statesml_Node> getStatesml_nodes() {
        return statesml_nodes;
    }

    public void addStatesml_node(Statesml_node statesml_node) {
        this.statesml_nodes.add(statesml_node);
    }
    public List<statesml_SystemUnits> getStatesml_systemunitss() {
        return statesml_systemunitss;
    }

    public void addStatesml_systemunits(Statesml_systemunits statesml_systemunits) {
        this.statesml_systemunitss.add(statesml_systemunits);
    }
    public List<statesml_Attribute> getStatesml_attributes() {
        return statesml_attributes;
    }

    public void addStatesml_attribute(Statesml_attribute statesml_attribute) {
        this.statesml_attributes.add(statesml_attribute);
    }

}