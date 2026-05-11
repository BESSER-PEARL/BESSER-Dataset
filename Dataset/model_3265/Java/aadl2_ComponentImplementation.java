





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComponentImplementation extends ComponentClassifier {

    private String noCalls;
    private String noConnections;
    private String noSubcomponents;





    private List<aadl2_SubprogramProxy> aadl2_subprogramproxys;




    private aadl2_ComponentImplementationReference aadl2_componentimplementationreference;




    private List<aadl2_InternalFeature> aadl2_internalfeatures;




    private List<aadl2_FlowImplementation> aadl2_flowimplementations;




    private aadl2_ComponentImplementation aadl2_componentimplementation;




    private List<aadl2_ProcessorFeature> aadl2_processorfeatures;




    private List<aadl2_Connection> aadl2_connections;




    private List<aadl2_Subcomponent> aadl2_subcomponents;


    public aadl2_ComponentImplementation(
        String noCalls,        String noConnections,        String noSubcomponents    ) {
        super(
        );
        this.noCalls = noCalls;
        this.noConnections = noConnections;
        this.noSubcomponents = noSubcomponents;
        this.aadl2_subprogramproxys = new ArrayList<>();
        this.aadl2_internalfeatures = new ArrayList<>();
        this.aadl2_flowimplementations = new ArrayList<>();
        this.aadl2_processorfeatures = new ArrayList<>();
        this.aadl2_connections = new ArrayList<>();
        this.aadl2_subcomponents = new ArrayList<>();
    }

    public aadl2_ComponentImplementation(
        String noCalls,        String noConnections,        String noSubcomponents        ArrayList<aadl2_SubprogramProxy> aadl2_subprogramproxys,        ArrayList<aadl2_InternalFeature> aadl2_internalfeatures,        ArrayList<aadl2_FlowImplementation> aadl2_flowimplementations,        ArrayList<aadl2_ProcessorFeature> aadl2_processorfeatures,        ArrayList<aadl2_Connection> aadl2_connections,        ArrayList<aadl2_Subcomponent> aadl2_subcomponents    ) {
        this.noCalls = noCalls;
        this.noConnections = noConnections;
        this.noSubcomponents = noSubcomponents;
        this.aadl2_subprogramproxys = aadl2_subprogramproxys;
        this.aadl2_internalfeatures = aadl2_internalfeatures;
        this.aadl2_flowimplementations = aadl2_flowimplementations;
        this.aadl2_processorfeatures = aadl2_processorfeatures;
        this.aadl2_connections = aadl2_connections;
        this.aadl2_subcomponents = aadl2_subcomponents;
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
    public String getNosubcomponents() {
        return noSubcomponents;
    }

    public void setNosubcomponents(String noSubcomponents) {
        this.noSubcomponents = noSubcomponents;
    }

    public List<aadl2_SubprogramProxy> getAadl2_subprogramproxys() {
        return aadl2_subprogramproxys;
    }

    public void addAadl2_subprogramproxy(Aadl2_subprogramproxy aadl2_subprogramproxy) {
        this.aadl2_subprogramproxys.add(aadl2_subprogramproxy);
    }
    public aadl2_ComponentImplementationReference getAadl2_componentimplementationreference() {
        return aadl2_componentimplementationreference;
    }

    public void setAadl2_componentimplementationreference(aadl2_ComponentImplementationReference aadl2_componentimplementationreference) {
        this.aadl2_componentimplementationreference = aadl2_componentimplementationreference;
    }
    public List<aadl2_InternalFeature> getAadl2_internalfeatures() {
        return aadl2_internalfeatures;
    }

    public void addAadl2_internalfeature(Aadl2_internalfeature aadl2_internalfeature) {
        this.aadl2_internalfeatures.add(aadl2_internalfeature);
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
    public List<aadl2_ProcessorFeature> getAadl2_processorfeatures() {
        return aadl2_processorfeatures;
    }

    public void addAadl2_processorfeature(Aadl2_processorfeature aadl2_processorfeature) {
        this.aadl2_processorfeatures.add(aadl2_processorfeature);
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

}