





import java.util.List;
import java.util.ArrayList;

public class jointPackage_PetriNet2PNML_TrgLabel extends TrgLocatedElement {

    private String text;





    private jointPackage_PetriNet2PNML_TrgLabeledElement jointpackage_petrinet2pnml_trglabeledelement;


    public jointPackage_PetriNet2PNML_TrgLabel(
        String text    ) {
        super(
        );
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public jointPackage_PetriNet2PNML_TrgLabeledElement getJointpackage_petrinet2pnml_trglabeledelement() {
        return jointpackage_petrinet2pnml_trglabeledelement;
    }

    public void setJointpackage_petrinet2pnml_trglabeledelement(jointPackage_PetriNet2PNML_TrgLabeledElement jointpackage_petrinet2pnml_trglabeledelement) {
        this.jointpackage_petrinet2pnml_trglabeledelement = jointpackage_petrinet2pnml_trglabeledelement;
    }

}