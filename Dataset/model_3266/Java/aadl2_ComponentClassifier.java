





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComponentClassifier extends SubcomponentType, Classifier, FeatureClassifier {

    private String noModes;
    private String noFlows;
    private String derivedModes;





    private List<aadl2_Mode> aadl2_modes;




    private List<aadl2_ModeTransition> aadl2_modetransitions;




    private aadl2_Subcomponent aadl2_subcomponent;


    public aadl2_ComponentClassifier(
        String noModes,        String noFlows,        String derivedModes    ) {
        super(
        );
        this.noModes = noModes;
        this.noFlows = noFlows;
        this.derivedModes = derivedModes;
        this.aadl2_modes = new ArrayList<>();
        this.aadl2_modetransitions = new ArrayList<>();
    }

    public aadl2_ComponentClassifier(
        String noModes,        String noFlows,        String derivedModes        ArrayList<aadl2_Mode> aadl2_modes,        ArrayList<aadl2_ModeTransition> aadl2_modetransitions    ) {
        this.noModes = noModes;
        this.noFlows = noFlows;
        this.derivedModes = derivedModes;
        this.aadl2_modes = aadl2_modes;
        this.aadl2_modetransitions = aadl2_modetransitions;
    }

    public String getNomodes() {
        return noModes;
    }

    public void setNomodes(String noModes) {
        this.noModes = noModes;
    }
    public String getNoflows() {
        return noFlows;
    }

    public void setNoflows(String noFlows) {
        this.noFlows = noFlows;
    }
    public String getDerivedmodes() {
        return derivedModes;
    }

    public void setDerivedmodes(String derivedModes) {
        this.derivedModes = derivedModes;
    }

    public List<aadl2_Mode> getAadl2_modes() {
        return aadl2_modes;
    }

    public void addAadl2_mode(Aadl2_mode aadl2_mode) {
        this.aadl2_modes.add(aadl2_mode);
    }
    public List<aadl2_ModeTransition> getAadl2_modetransitions() {
        return aadl2_modetransitions;
    }

    public void addAadl2_modetransition(Aadl2_modetransition aadl2_modetransition) {
        this.aadl2_modetransitions.add(aadl2_modetransition);
    }
    public aadl2_Subcomponent getAadl2_subcomponent() {
        return aadl2_subcomponent;
    }

    public void setAadl2_subcomponent(aadl2_Subcomponent aadl2_subcomponent) {
        this.aadl2_subcomponent = aadl2_subcomponent;
    }

}