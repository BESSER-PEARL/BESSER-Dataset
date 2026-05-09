





import java.util.List;
import java.util.ArrayList;

public class jointPackage_PetriNet2PNML_TrgURI extends TrgLocatedElement {

    private String value;





    private jointPackage_PetriNet2PNML_TrgPNMLDocument jointpackage_petrinet2pnml_trgpnmldocument;


    public jointPackage_PetriNet2PNML_TrgURI(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public jointPackage_PetriNet2PNML_TrgPNMLDocument getJointpackage_petrinet2pnml_trgpnmldocument() {
        return jointpackage_petrinet2pnml_trgpnmldocument;
    }

    public void setJointpackage_petrinet2pnml_trgpnmldocument(jointPackage_PetriNet2PNML_TrgPNMLDocument jointpackage_petrinet2pnml_trgpnmldocument) {
        this.jointpackage_petrinet2pnml_trgpnmldocument = jointpackage_petrinet2pnml_trgpnmldocument;
    }

}