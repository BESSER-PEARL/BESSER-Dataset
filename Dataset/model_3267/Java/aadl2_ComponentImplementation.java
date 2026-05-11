





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComponentImplementation extends ComponentClassifier {

    private String noCalls;
    private String noConnections;
    private String noSubcomponents;





    private List<aadl2_EventSource> aadl2_eventsources;




    private List<aadl2_Subcomponent> aadl2_subcomponents;




    private List<aadl2_EndToEndFlow> aadl2_endtoendflows;




    private List<aadl2_AbstractSubcomponent> aadl2_abstractsubcomponents;




    private List<aadl2_InternalFeature> aadl2_internalfeatures;




    private aadl2_ComponentImplementation aadl2_componentimplementation;




    private List<aadl2_EventDataSource> aadl2_eventdatasources;




    private List<aadl2_Connection> aadl2_connections;




    private List<aadl2_FlowImplementation> aadl2_flowimplementations;




    private List<aadl2_PortConnection> aadl2_portconnections;




    private List<aadl2_ProcessorFeature> aadl2_processorfeatures;




    private aadl2_ComponentImplementationReference aadl2_componentimplementationreference;




    private List<aadl2_FeatureConnection> aadl2_featureconnections;




    private List<aadl2_AccessConnection> aadl2_accessconnections;




    private List<aadl2_FeatureGroupConnection> aadl2_featuregroupconnections;




    private aadl2_Realization aadl2_realization;




    private aadl2_ImplementationExtension aadl2_implementationextension;




    private List<aadl2_SubprogramProxy> aadl2_subprogramproxys;




    private aadl2_ImplementationExtension aadl2_implementationextension;




    private List<aadl2_ParameterConnection> aadl2_parameterconnections;




    private List<aadl2_PortProxy> aadl2_portproxys;


    public aadl2_ComponentImplementation(
        String noCalls,        String noConnections,        String noSubcomponents    ) {
        super(
        );
        this.noCalls = noCalls;
        this.noConnections = noConnections;
        this.noSubcomponents = noSubcomponents;
        this.aadl2_eventsources = new ArrayList<>();
        this.aadl2_subcomponents = new ArrayList<>();
        this.aadl2_endtoendflows = new ArrayList<>();
        this.aadl2_abstractsubcomponents = new ArrayList<>();
        this.aadl2_internalfeatures = new ArrayList<>();
        this.aadl2_eventdatasources = new ArrayList<>();
        this.aadl2_connections = new ArrayList<>();
        this.aadl2_flowimplementations = new ArrayList<>();
        this.aadl2_portconnections = new ArrayList<>();
        this.aadl2_processorfeatures = new ArrayList<>();
        this.aadl2_featureconnections = new ArrayList<>();
        this.aadl2_accessconnections = new ArrayList<>();
        this.aadl2_featuregroupconnections = new ArrayList<>();
        this.aadl2_subprogramproxys = new ArrayList<>();
        this.aadl2_parameterconnections = new ArrayList<>();
        this.aadl2_portproxys = new ArrayList<>();
    }

    public aadl2_ComponentImplementation(
        String noCalls,        String noConnections,        String noSubcomponents        ArrayList<aadl2_EventSource> aadl2_eventsources,        ArrayList<aadl2_Subcomponent> aadl2_subcomponents,        ArrayList<aadl2_EndToEndFlow> aadl2_endtoendflows,        ArrayList<aadl2_AbstractSubcomponent> aadl2_abstractsubcomponents,        ArrayList<aadl2_InternalFeature> aadl2_internalfeatures,        ArrayList<aadl2_EventDataSource> aadl2_eventdatasources,        ArrayList<aadl2_Connection> aadl2_connections,        ArrayList<aadl2_FlowImplementation> aadl2_flowimplementations,        ArrayList<aadl2_PortConnection> aadl2_portconnections,        ArrayList<aadl2_ProcessorFeature> aadl2_processorfeatures,        ArrayList<aadl2_FeatureConnection> aadl2_featureconnections,        ArrayList<aadl2_AccessConnection> aadl2_accessconnections,        ArrayList<aadl2_FeatureGroupConnection> aadl2_featuregroupconnections,        ArrayList<aadl2_SubprogramProxy> aadl2_subprogramproxys,        ArrayList<aadl2_ParameterConnection> aadl2_parameterconnections,        ArrayList<aadl2_PortProxy> aadl2_portproxys    ) {
        this.noCalls = noCalls;
        this.noConnections = noConnections;
        this.noSubcomponents = noSubcomponents;
        this.aadl2_eventsources = aadl2_eventsources;
        this.aadl2_subcomponents = aadl2_subcomponents;
        this.aadl2_endtoendflows = aadl2_endtoendflows;
        this.aadl2_abstractsubcomponents = aadl2_abstractsubcomponents;
        this.aadl2_internalfeatures = aadl2_internalfeatures;
        this.aadl2_eventdatasources = aadl2_eventdatasources;
        this.aadl2_connections = aadl2_connections;
        this.aadl2_flowimplementations = aadl2_flowimplementations;
        this.aadl2_portconnections = aadl2_portconnections;
        this.aadl2_processorfeatures = aadl2_processorfeatures;
        this.aadl2_featureconnections = aadl2_featureconnections;
        this.aadl2_accessconnections = aadl2_accessconnections;
        this.aadl2_featuregroupconnections = aadl2_featuregroupconnections;
        this.aadl2_subprogramproxys = aadl2_subprogramproxys;
        this.aadl2_parameterconnections = aadl2_parameterconnections;
        this.aadl2_portproxys = aadl2_portproxys;
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

    public List<aadl2_EventSource> getAadl2_eventsources() {
        return aadl2_eventsources;
    }

    public void addAadl2_eventsource(Aadl2_eventsource aadl2_eventsource) {
        this.aadl2_eventsources.add(aadl2_eventsource);
    }
    public List<aadl2_Subcomponent> getAadl2_subcomponents() {
        return aadl2_subcomponents;
    }

    public void addAadl2_subcomponent(Aadl2_subcomponent aadl2_subcomponent) {
        this.aadl2_subcomponents.add(aadl2_subcomponent);
    }
    public List<aadl2_EndToEndFlow> getAadl2_endtoendflows() {
        return aadl2_endtoendflows;
    }

    public void addAadl2_endtoendflow(Aadl2_endtoendflow aadl2_endtoendflow) {
        this.aadl2_endtoendflows.add(aadl2_endtoendflow);
    }
    public List<aadl2_AbstractSubcomponent> getAadl2_abstractsubcomponents() {
        return aadl2_abstractsubcomponents;
    }

    public void addAadl2_abstractsubcomponent(Aadl2_abstractsubcomponent aadl2_abstractsubcomponent) {
        this.aadl2_abstractsubcomponents.add(aadl2_abstractsubcomponent);
    }
    public List<aadl2_InternalFeature> getAadl2_internalfeatures() {
        return aadl2_internalfeatures;
    }

    public void addAadl2_internalfeature(Aadl2_internalfeature aadl2_internalfeature) {
        this.aadl2_internalfeatures.add(aadl2_internalfeature);
    }
    public aadl2_ComponentImplementation getAadl2_componentimplementation() {
        return aadl2_componentimplementation;
    }

    public void setAadl2_componentimplementation(aadl2_ComponentImplementation aadl2_componentimplementation) {
        this.aadl2_componentimplementation = aadl2_componentimplementation;
    }
    public List<aadl2_EventDataSource> getAadl2_eventdatasources() {
        return aadl2_eventdatasources;
    }

    public void addAadl2_eventdatasource(Aadl2_eventdatasource aadl2_eventdatasource) {
        this.aadl2_eventdatasources.add(aadl2_eventdatasource);
    }
    public List<aadl2_Connection> getAadl2_connections() {
        return aadl2_connections;
    }

    public void addAadl2_connection(Aadl2_connection aadl2_connection) {
        this.aadl2_connections.add(aadl2_connection);
    }
    public List<aadl2_FlowImplementation> getAadl2_flowimplementations() {
        return aadl2_flowimplementations;
    }

    public void addAadl2_flowimplementation(Aadl2_flowimplementation aadl2_flowimplementation) {
        this.aadl2_flowimplementations.add(aadl2_flowimplementation);
    }
    public List<aadl2_PortConnection> getAadl2_portconnections() {
        return aadl2_portconnections;
    }

    public void addAadl2_portconnection(Aadl2_portconnection aadl2_portconnection) {
        this.aadl2_portconnections.add(aadl2_portconnection);
    }
    public List<aadl2_ProcessorFeature> getAadl2_processorfeatures() {
        return aadl2_processorfeatures;
    }

    public void addAadl2_processorfeature(Aadl2_processorfeature aadl2_processorfeature) {
        this.aadl2_processorfeatures.add(aadl2_processorfeature);
    }
    public aadl2_ComponentImplementationReference getAadl2_componentimplementationreference() {
        return aadl2_componentimplementationreference;
    }

    public void setAadl2_componentimplementationreference(aadl2_ComponentImplementationReference aadl2_componentimplementationreference) {
        this.aadl2_componentimplementationreference = aadl2_componentimplementationreference;
    }
    public List<aadl2_FeatureConnection> getAadl2_featureconnections() {
        return aadl2_featureconnections;
    }

    public void addAadl2_featureconnection(Aadl2_featureconnection aadl2_featureconnection) {
        this.aadl2_featureconnections.add(aadl2_featureconnection);
    }
    public List<aadl2_AccessConnection> getAadl2_accessconnections() {
        return aadl2_accessconnections;
    }

    public void addAadl2_accessconnection(Aadl2_accessconnection aadl2_accessconnection) {
        this.aadl2_accessconnections.add(aadl2_accessconnection);
    }
    public List<aadl2_FeatureGroupConnection> getAadl2_featuregroupconnections() {
        return aadl2_featuregroupconnections;
    }

    public void addAadl2_featuregroupconnection(Aadl2_featuregroupconnection aadl2_featuregroupconnection) {
        this.aadl2_featuregroupconnections.add(aadl2_featuregroupconnection);
    }
    public aadl2_Realization getAadl2_realization() {
        return aadl2_realization;
    }

    public void setAadl2_realization(aadl2_Realization aadl2_realization) {
        this.aadl2_realization = aadl2_realization;
    }
    public aadl2_ImplementationExtension getAadl2_implementationextension() {
        return aadl2_implementationextension;
    }

    public void setAadl2_implementationextension(aadl2_ImplementationExtension aadl2_implementationextension) {
        this.aadl2_implementationextension = aadl2_implementationextension;
    }
    public List<aadl2_SubprogramProxy> getAadl2_subprogramproxys() {
        return aadl2_subprogramproxys;
    }

    public void addAadl2_subprogramproxy(Aadl2_subprogramproxy aadl2_subprogramproxy) {
        this.aadl2_subprogramproxys.add(aadl2_subprogramproxy);
    }
    public aadl2_ImplementationExtension getAadl2_implementationextension() {
        return aadl2_implementationextension;
    }

    public void setAadl2_implementationextension(aadl2_ImplementationExtension aadl2_implementationextension) {
        this.aadl2_implementationextension = aadl2_implementationextension;
    }
    public List<aadl2_ParameterConnection> getAadl2_parameterconnections() {
        return aadl2_parameterconnections;
    }

    public void addAadl2_parameterconnection(Aadl2_parameterconnection aadl2_parameterconnection) {
        this.aadl2_parameterconnections.add(aadl2_parameterconnection);
    }
    public List<aadl2_PortProxy> getAadl2_portproxys() {
        return aadl2_portproxys;
    }

    public void addAadl2_portproxy(Aadl2_portproxy aadl2_portproxy) {
        this.aadl2_portproxys.add(aadl2_portproxy);
    }

}