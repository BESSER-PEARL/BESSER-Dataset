





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComponentClassifier extends Classifier, SubcomponentType, FeatureClassifier {

    private String noFlows;
    private String derivedModes;
    private String noModes;





    private aadl2_Subcomponent aadl2_subcomponent;




    private List<aadl2_ModeTransition> aadl2_modetransitions;




    private List<aadl2_Mode> aadl2_modes;


    public aadl2_ComponentClassifier(
        String noFlows,        String derivedModes,        String noModes    ) {
        super(
        );
        this.noFlows = noFlows;
        this.derivedModes = derivedModes;
        this.noModes = noModes;
        this.aadl2_modetransitions = new ArrayList<>();
        this.aadl2_modes = new ArrayList<>();
    }

    public aadl2_ComponentClassifier(
        String noFlows,        String derivedModes,        String noModes        ArrayList<aadl2_ModeTransition> aadl2_modetransitions,        ArrayList<aadl2_Mode> aadl2_modes    ) {
        this.noFlows = noFlows;
        this.derivedModes = derivedModes;
        this.noModes = noModes;
        this.aadl2_modetransitions = aadl2_modetransitions;
        this.aadl2_modes = aadl2_modes;
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
    public String getNomodes() {
        return noModes;
    }

    public void setNomodes(String noModes) {
        this.noModes = noModes;
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
    public List<aadl2_Mode> getAadl2_modes() {
        return aadl2_modes;
    }

    public void addAadl2_mode(Aadl2_mode aadl2_mode) {
        this.aadl2_modes.add(aadl2_mode);
    }

}