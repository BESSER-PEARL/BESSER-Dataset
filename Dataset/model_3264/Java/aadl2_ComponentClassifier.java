





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComponentClassifier extends FeatureClassifier, Classifier, SubcomponentType {

    private String noFlows;
    private String noModes;
    private String derivedModes;





    private aadl2_PortSpecification aadl2_portspecification;




    private List<aadl2_Mode> aadl2_modes;




    private aadl2_Subcomponent aadl2_subcomponent;




    private List<aadl2_ModeTransition> aadl2_modetransitions;




    private aadl2_AccessSpecification aadl2_accessspecification;


    public aadl2_ComponentClassifier(
        String noFlows,        String noModes,        String derivedModes    ) {
        super(
        );
        this.noFlows = noFlows;
        this.noModes = noModes;
        this.derivedModes = derivedModes;
        this.aadl2_modes = new ArrayList<>();
        this.aadl2_modetransitions = new ArrayList<>();
    }

    public aadl2_ComponentClassifier(
        String noFlows,        String noModes,        String derivedModes        ArrayList<aadl2_Mode> aadl2_modes,        ArrayList<aadl2_ModeTransition> aadl2_modetransitions    ) {
        this.noFlows = noFlows;
        this.noModes = noModes;
        this.derivedModes = derivedModes;
        this.aadl2_modes = aadl2_modes;
        this.aadl2_modetransitions = aadl2_modetransitions;
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
    public String getDerivedmodes() {
        return derivedModes;
    }

    public void setDerivedmodes(String derivedModes) {
        this.derivedModes = derivedModes;
    }

    public aadl2_PortSpecification getAadl2_portspecification() {
        return aadl2_portspecification;
    }

    public void setAadl2_portspecification(aadl2_PortSpecification aadl2_portspecification) {
        this.aadl2_portspecification = aadl2_portspecification;
    }
    public List<aadl2_Mode> getAadl2_modes() {
        return aadl2_modes;
    }

    public void addAadl2_mode(Aadl2_mode aadl2_mode) {
        this.aadl2_modes.add(aadl2_mode);
    }
    public aadl2_Subcomponent getAadl2_subcomponent() {
        return aadl2_subcomponent;
    }

    public void setAadl2_subcomponent(aadl2_Subcomponent aadl2_subcomponent) {
        this.aadl2_subcomponent = aadl2_subcomponent;
    }
    public List<aadl2_ModeTransition> getAadl2_modetransitions() {
        return aadl2_modetransitions;
    }

    public void addAadl2_modetransition(Aadl2_modetransition aadl2_modetransition) {
        this.aadl2_modetransitions.add(aadl2_modetransition);
    }
    public aadl2_AccessSpecification getAadl2_accessspecification() {
        return aadl2_accessspecification;
    }

    public void setAadl2_accessspecification(aadl2_AccessSpecification aadl2_accessspecification) {
        this.aadl2_accessspecification = aadl2_accessspecification;
    }

}