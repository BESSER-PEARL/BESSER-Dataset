





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComponentClassifier extends Classifier, SubcomponentType, FeatureClassifier {

    private String noModes;
    private String derivedModes;
    private String noFlows;





    private aadl2_Subcomponent aadl2_subcomponent;




    private List<aadl2_ModeTransition> aadl2_modetransitions;


    public aadl2_ComponentClassifier(
        String noModes,        String derivedModes,        String noFlows    ) {
        super(
        );
        this.noModes = noModes;
        this.derivedModes = derivedModes;
        this.noFlows = noFlows;
        this.aadl2_modetransitions = new ArrayList<>();
    }

    public aadl2_ComponentClassifier(
        String noModes,        String derivedModes,        String noFlows        ArrayList<aadl2_ModeTransition> aadl2_modetransitions    ) {
        this.noModes = noModes;
        this.derivedModes = derivedModes;
        this.noFlows = noFlows;
        this.aadl2_modetransitions = aadl2_modetransitions;
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
    public String getNoflows() {
        return noFlows;
    }

    public void setNoflows(String noFlows) {
        this.noFlows = noFlows;
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

}