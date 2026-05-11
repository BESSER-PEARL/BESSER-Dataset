





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComponentClassifier extends Classifier {

    private String noFlows;
    private String noModes;





    private aadl2_AbstractFeature aadl2_abstractfeature;




    private aadl2_ComponentReference aadl2_componentreference;




    private List<aadl2_InternalEvent> aadl2_internalevents;




    private List<aadl2_ProcessorPort> aadl2_processorports;




    private aadl2_Subcomponent aadl2_subcomponent;




    private aadl2_AccessSpecification aadl2_accessspecification;




    private aadl2_PortSpecification aadl2_portspecification;




    private List<aadl2_ModeTransition> aadl2_modetransitions;




    private aadl2_FeaturePrototype aadl2_featureprototype;




    private aadl2_Feature aadl2_feature;




    private List<aadl2_Mode> aadl2_modes;


    public aadl2_ComponentClassifier(
        String noFlows,        String noModes    ) {
        super(
        );
        this.noFlows = noFlows;
        this.noModes = noModes;
        this.aadl2_internalevents = new ArrayList<>();
        this.aadl2_processorports = new ArrayList<>();
        this.aadl2_modetransitions = new ArrayList<>();
        this.aadl2_modes = new ArrayList<>();
    }

    public aadl2_ComponentClassifier(
        String noFlows,        String noModes        ArrayList<aadl2_InternalEvent> aadl2_internalevents,        ArrayList<aadl2_ProcessorPort> aadl2_processorports,        ArrayList<aadl2_ModeTransition> aadl2_modetransitions,        ArrayList<aadl2_Mode> aadl2_modes    ) {
        this.noFlows = noFlows;
        this.noModes = noModes;
        this.aadl2_internalevents = aadl2_internalevents;
        this.aadl2_processorports = aadl2_processorports;
        this.aadl2_modetransitions = aadl2_modetransitions;
        this.aadl2_modes = aadl2_modes;
    }

    public String getNoflows() {
        return noFlows;
    }

    public void setNoflows(String noFlows) {
        this.noFlows = noFlows;
    }
    public String getNomodes() {
        return noModes;
    }

    public void setNomodes(String noModes) {
        this.noModes = noModes;
    }

    public aadl2_AbstractFeature getAadl2_abstractfeature() {
        return aadl2_abstractfeature;
    }

    public void setAadl2_abstractfeature(aadl2_AbstractFeature aadl2_abstractfeature) {
        this.aadl2_abstractfeature = aadl2_abstractfeature;
    }
    public aadl2_ComponentReference getAadl2_componentreference() {
        return aadl2_componentreference;
    }

    public void setAadl2_componentreference(aadl2_ComponentReference aadl2_componentreference) {
        this.aadl2_componentreference = aadl2_componentreference;
    }
    public List<aadl2_InternalEvent> getAadl2_internalevents() {
        return aadl2_internalevents;
    }

    public void addAadl2_internalevent(Aadl2_internalevent aadl2_internalevent) {
        this.aadl2_internalevents.add(aadl2_internalevent);
    }
    public List<aadl2_ProcessorPort> getAadl2_processorports() {
        return aadl2_processorports;
    }

    public void addAadl2_processorport(Aadl2_processorport aadl2_processorport) {
        this.aadl2_processorports.add(aadl2_processorport);
    }
    public aadl2_Subcomponent getAadl2_subcomponent() {
        return aadl2_subcomponent;
    }

    public void setAadl2_subcomponent(aadl2_Subcomponent aadl2_subcomponent) {
        this.aadl2_subcomponent = aadl2_subcomponent;
    }
    public aadl2_AccessSpecification getAadl2_accessspecification() {
        return aadl2_accessspecification;
    }

    public void setAadl2_accessspecification(aadl2_AccessSpecification aadl2_accessspecification) {
        this.aadl2_accessspecification = aadl2_accessspecification;
    }
    public aadl2_PortSpecification getAadl2_portspecification() {
        return aadl2_portspecification;
    }

    public void setAadl2_portspecification(aadl2_PortSpecification aadl2_portspecification) {
        this.aadl2_portspecification = aadl2_portspecification;
    }
    public List<aadl2_ModeTransition> getAadl2_modetransitions() {
        return aadl2_modetransitions;
    }

    public void addAadl2_modetransition(Aadl2_modetransition aadl2_modetransition) {
        this.aadl2_modetransitions.add(aadl2_modetransition);
    }
    public aadl2_FeaturePrototype getAadl2_featureprototype() {
        return aadl2_featureprototype;
    }

    public void setAadl2_featureprototype(aadl2_FeaturePrototype aadl2_featureprototype) {
        this.aadl2_featureprototype = aadl2_featureprototype;
    }
    public aadl2_Feature getAadl2_feature() {
        return aadl2_feature;
    }

    public void setAadl2_feature(aadl2_Feature aadl2_feature) {
        this.aadl2_feature = aadl2_feature;
    }
    public List<aadl2_Mode> getAadl2_modes() {
        return aadl2_modes;
    }

    public void addAadl2_mode(Aadl2_mode aadl2_mode) {
        this.aadl2_modes.add(aadl2_mode);
    }

}