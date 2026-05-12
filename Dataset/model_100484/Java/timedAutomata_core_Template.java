





import java.util.List;
import java.util.ArrayList;

public class timedAutomata_core_Template extends base_Nameable, core_TAElement, base_Identifyable {






    private List<core_timedAutomata_Parameter> core_timedautomata_parameters;




    private List<Edge> edges;


    public timedAutomata_core_Template(
    ) {
        super(
        );
        this.core_timedautomata_parameters = new ArrayList<>();
        this.edges = new ArrayList<>();
    }

    public timedAutomata_core_Template(
        ArrayList<core_timedAutomata_Parameter> core_timedautomata_parameters,        ArrayList<Edge> edges    ) {
        this.core_timedautomata_parameters = core_timedautomata_parameters;
        this.edges = edges;
    }


    public List<core_timedAutomata_Parameter> getCore_timedautomata_parameters() {
        return core_timedautomata_parameters;
    }

    public void addCore_timedautomata_parameter(Core_timedautomata_parameter core_timedautomata_parameter) {
        this.core_timedautomata_parameters.add(core_timedautomata_parameter);
    }
    public List<Edge> getEdges() {
        return edges;
    }

    public void addEdge(Edge edge) {
        this.edges.add(edge);
    }

}