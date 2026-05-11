





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComponentImplementation extends ComponentClassifier {

    private String connections;
    private String flows;
    private String noSubcomponents;
    private String noCalls;
    private String noConnections;
    private String subcomponents;





    private List<aadl2_Connection> aadl2_connections;




    private List<aadl2_Subcomponent> aadl2_subcomponents;




    private List<aadl2_FlowImplementation> aadl2_flowimplementations;




    private aadl2_ComponentImplementation aadl2_componentimplementation;




    private aadl2_ComponentImplementationReference aadl2_componentimplementationreference;


    public aadl2_ComponentImplementation(
        String connections,        String flows,        String noSubcomponents,        String noCalls,        String noConnections,        String subcomponents    ) {
        super(
        );
        this.connections = connections;
        this.flows = flows;
        this.noSubcomponents = noSubcomponents;
        this.noCalls = noCalls;
        this.noConnections = noConnections;
        this.subcomponents = subcomponents;
        this.aadl2_connections = new ArrayList<>();
        this.aadl2_subcomponents = new ArrayList<>();
        this.aadl2_flowimplementations = new ArrayList<>();
    }

    public aadl2_ComponentImplementation(
        String connections,        String flows,        String noSubcomponents,        String noCalls,        String noConnections,        String subcomponents        ArrayList<aadl2_Connection> aadl2_connections,        ArrayList<aadl2_Subcomponent> aadl2_subcomponents,        ArrayList<aadl2_FlowImplementation> aadl2_flowimplementations    ) {
        this.connections = connections;
        this.flows = flows;
        this.noSubcomponents = noSubcomponents;
        this.noCalls = noCalls;
        this.noConnections = noConnections;
        this.subcomponents = subcomponents;
        this.aadl2_connections = aadl2_connections;
        this.aadl2_subcomponents = aadl2_subcomponents;
        this.aadl2_flowimplementations = aadl2_flowimplementations;
    }

    public String getConnections() {
        return connections;
    }

    public void setConnections(String connections) {
        this.connections = connections;
    }
    public String getFlows() {
        return flows;
    }

    public void setFlows(String flows) {
        this.flows = flows;
    }
    public String getNosubcomponents() {
        return noSubcomponents;
    }

    public void setNosubcomponents(String noSubcomponents) {
        this.noSubcomponents = noSubcomponents;
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
    public String getSubcomponents() {
        return subcomponents;
    }

    public void setSubcomponents(String subcomponents) {
        this.subcomponents = subcomponents;
    }

    public List<aadl2_Connection> getAadl2_connections() {
        return aadl2_connections;
    }

    public void addAadl2_connection(Aadl2_connection aadl2_connection) {
        this.aadl2_connections.add(aadl2_connection);
    }
    public List<aadl2_Subcomponent> getAadl2_subcomponents() {
        return aadl2_subcomponents;
    }

    public void addAadl2_subcomponent(Aadl2_subcomponent aadl2_subcomponent) {
        this.aadl2_subcomponents.add(aadl2_subcomponent);
    }
    public List<aadl2_FlowImplementation> getAadl2_flowimplementations() {
        return aadl2_flowimplementations;
    }

    public void addAadl2_flowimplementation(Aadl2_flowimplementation aadl2_flowimplementation) {
        this.aadl2_flowimplementations.add(aadl2_flowimplementation);
    }
    public aadl2_ComponentImplementation getAadl2_componentimplementation() {
        return aadl2_componentimplementation;
    }

    public void setAadl2_componentimplementation(aadl2_ComponentImplementation aadl2_componentimplementation) {
        this.aadl2_componentimplementation = aadl2_componentimplementation;
    }
    public aadl2_ComponentImplementationReference getAadl2_componentimplementationreference() {
        return aadl2_componentimplementationreference;
    }

    public void setAadl2_componentimplementationreference(aadl2_ComponentImplementationReference aadl2_componentimplementationreference) {
        this.aadl2_componentimplementationreference = aadl2_componentimplementationreference;
    }

}