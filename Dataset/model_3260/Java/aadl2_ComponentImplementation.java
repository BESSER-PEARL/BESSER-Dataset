





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComponentImplementation extends ComponentClassifier {

    private String connections;
    private String noCalls;
    private String noConnections;
    private String flows;
    private String subcomponents;
    private String noSubcomponents;





    private aadl2_ComponentImplementation aadl2_componentimplementation;




    private List<aadl2_Connection> aadl2_connections;




    private aadl2_ComponentImplementationReference aadl2_componentimplementationreference;




    private List<aadl2_FlowImplementation> aadl2_flowimplementations;




    private List<aadl2_Subcomponent> aadl2_subcomponents;


    public aadl2_ComponentImplementation(
        String connections,        String noCalls,        String noConnections,        String flows,        String subcomponents,        String noSubcomponents    ) {
        super(
        );
        this.connections = connections;
        this.noCalls = noCalls;
        this.noConnections = noConnections;
        this.flows = flows;
        this.subcomponents = subcomponents;
        this.noSubcomponents = noSubcomponents;
        this.aadl2_connections = new ArrayList<>();
        this.aadl2_flowimplementations = new ArrayList<>();
        this.aadl2_subcomponents = new ArrayList<>();
    }

    public aadl2_ComponentImplementation(
        String connections,        String noCalls,        String noConnections,        String flows,        String subcomponents,        String noSubcomponents        ArrayList<aadl2_Connection> aadl2_connections,        ArrayList<aadl2_FlowImplementation> aadl2_flowimplementations,        ArrayList<aadl2_Subcomponent> aadl2_subcomponents    ) {
        this.connections = connections;
        this.noCalls = noCalls;
        this.noConnections = noConnections;
        this.flows = flows;
        this.subcomponents = subcomponents;
        this.noSubcomponents = noSubcomponents;
        this.aadl2_connections = aadl2_connections;
        this.aadl2_flowimplementations = aadl2_flowimplementations;
        this.aadl2_subcomponents = aadl2_subcomponents;
    }

    public String getConnections() {
        return connections;
    }

    public void setConnections(String connections) {
        this.connections = connections;
    }
    public String getNocalls() {
        return noCalls;
    }

    public void setNocalls(String noCalls) {
        this.noCalls = noCalls;
    }
    public String getNoconnections() {
        return noConnections;
    }

    public void setNoconnections(String noConnections) {
        this.noConnections = noConnections;
    }
    public String getFlows() {
        return flows;
    }

    public void setFlows(String flows) {
        this.flows = flows;
    }
    public String getSubcomponents() {
        return subcomponents;
    }

    public void setSubcomponents(String subcomponents) {
        this.subcomponents = subcomponents;
    }
    public String getNosubcomponents() {
        return noSubcomponents;
    }

    public void setNosubcomponents(String noSubcomponents) {
        this.noSubcomponents = noSubcomponents;
    }

    public aadl2_ComponentImplementation getAadl2_componentimplementation() {
        return aadl2_componentimplementation;
    }

    public void setAadl2_componentimplementation(aadl2_ComponentImplementation aadl2_componentimplementation) {
        this.aadl2_componentimplementation = aadl2_componentimplementation;
    }
    public List<aadl2_Connection> getAadl2_connections() {
        return aadl2_connections;
    }

    public void addAadl2_connection(Aadl2_connection aadl2_connection) {
        this.aadl2_connections.add(aadl2_connection);
    }
    public aadl2_ComponentImplementationReference getAadl2_componentimplementationreference() {
        return aadl2_componentimplementationreference;
    }

    public void setAadl2_componentimplementationreference(aadl2_ComponentImplementationReference aadl2_componentimplementationreference) {
        this.aadl2_componentimplementationreference = aadl2_componentimplementationreference;
    }
    public List<aadl2_FlowImplementation> getAadl2_flowimplementations() {
        return aadl2_flowimplementations;
    }

    public void addAadl2_flowimplementation(Aadl2_flowimplementation aadl2_flowimplementation) {
        this.aadl2_flowimplementations.add(aadl2_flowimplementation);
    }
    public List<aadl2_Subcomponent> getAadl2_subcomponents() {
        return aadl2_subcomponents;
    }

    public void addAadl2_subcomponent(Aadl2_subcomponent aadl2_subcomponent) {
        this.aadl2_subcomponents.add(aadl2_subcomponent);
    }

}