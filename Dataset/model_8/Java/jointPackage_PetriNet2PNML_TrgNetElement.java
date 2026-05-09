





import java.util.List;
import java.util.ArrayList;

public class jointPackage_PetriNet2PNML_TrgNetElement extends TrgIdedElement {






    private jointPackage_PetriNet2PNML_TrgURI jointpackage_petrinet2pnml_trguri;




    private jointPackage_PetriNet2PNML_TrgPNMLDocument jointpackage_petrinet2pnml_trgpnmldocument;




    private List<jointPackage_PetriNet2PNML_TrgNetContent> jointpackage_petrinet2pnml_trgnetcontents;


    public jointPackage_PetriNet2PNML_TrgNetElement(
    ) {
        super(
        );
        this.jointpackage_petrinet2pnml_trgnetcontents = new ArrayList<>();
    }

    public jointPackage_PetriNet2PNML_TrgNetElement(
        ArrayList<jointPackage_PetriNet2PNML_TrgNetContent> jointpackage_petrinet2pnml_trgnetcontents    ) {
        this.jointpackage_petrinet2pnml_trgnetcontents = jointpackage_petrinet2pnml_trgnetcontents;
    }


    public jointPackage_PetriNet2PNML_TrgURI getJointpackage_petrinet2pnml_trguri() {
        return jointpackage_petrinet2pnml_trguri;
    }

    public void setJointpackage_petrinet2pnml_trguri(jointPackage_PetriNet2PNML_TrgURI jointpackage_petrinet2pnml_trguri) {
        this.jointpackage_petrinet2pnml_trguri = jointpackage_petrinet2pnml_trguri;
    }
    public jointPackage_PetriNet2PNML_TrgPNMLDocument getJointpackage_petrinet2pnml_trgpnmldocument() {
        return jointpackage_petrinet2pnml_trgpnmldocument;
    }

    public void setJointpackage_petrinet2pnml_trgpnmldocument(jointPackage_PetriNet2PNML_TrgPNMLDocument jointpackage_petrinet2pnml_trgpnmldocument) {
        this.jointpackage_petrinet2pnml_trgpnmldocument = jointpackage_petrinet2pnml_trgpnmldocument;
    }
    public List<jointPackage_PetriNet2PNML_TrgNetContent> getJointpackage_petrinet2pnml_trgnetcontents() {
        return jointpackage_petrinet2pnml_trgnetcontents;
    }

    public void addJointpackage_petrinet2pnml_trgnetcontent(Jointpackage_petrinet2pnml_trgnetcontent jointpackage_petrinet2pnml_trgnetcontent) {
        this.jointpackage_petrinet2pnml_trgnetcontents.add(jointpackage_petrinet2pnml_trgnetcontent);
    }

}