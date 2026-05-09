





import java.util.List;
import java.util.ArrayList;

public class jointPackage_PetriNet2PNML_SrcPlace extends SrcElement {






    private jointPackage_PetriNet2PNML_SrcTransitionToPlace jointpackage_petrinet2pnml_srctransitiontoplace;




    private jointPackage_PetriNet2PNML_SrcPlaceToTransition jointpackage_petrinet2pnml_srcplacetotransition;




    private List<jointPackage_PetriNet2PNML_SrcTransitionToPlace> jointpackage_petrinet2pnml_srctransitiontoplaces;




    private List<jointPackage_PetriNet2PNML_SrcPlaceToTransition> jointpackage_petrinet2pnml_srcplacetotransitions;


    public jointPackage_PetriNet2PNML_SrcPlace(
    ) {
        super(
        );
        this.jointpackage_petrinet2pnml_srctransitiontoplaces = new ArrayList<>();
        this.jointpackage_petrinet2pnml_srcplacetotransitions = new ArrayList<>();
    }

    public jointPackage_PetriNet2PNML_SrcPlace(
        ArrayList<jointPackage_PetriNet2PNML_SrcTransitionToPlace> jointpackage_petrinet2pnml_srctransitiontoplaces,        ArrayList<jointPackage_PetriNet2PNML_SrcPlaceToTransition> jointpackage_petrinet2pnml_srcplacetotransitions    ) {
        this.jointpackage_petrinet2pnml_srctransitiontoplaces = jointpackage_petrinet2pnml_srctransitiontoplaces;
        this.jointpackage_petrinet2pnml_srcplacetotransitions = jointpackage_petrinet2pnml_srcplacetotransitions;
    }


    public jointPackage_PetriNet2PNML_SrcTransitionToPlace getJointpackage_petrinet2pnml_srctransitiontoplace() {
        return jointpackage_petrinet2pnml_srctransitiontoplace;
    }

    public void setJointpackage_petrinet2pnml_srctransitiontoplace(jointPackage_PetriNet2PNML_SrcTransitionToPlace jointpackage_petrinet2pnml_srctransitiontoplace) {
        this.jointpackage_petrinet2pnml_srctransitiontoplace = jointpackage_petrinet2pnml_srctransitiontoplace;
    }
    public jointPackage_PetriNet2PNML_SrcPlaceToTransition getJointpackage_petrinet2pnml_srcplacetotransition() {
        return jointpackage_petrinet2pnml_srcplacetotransition;
    }

    public void setJointpackage_petrinet2pnml_srcplacetotransition(jointPackage_PetriNet2PNML_SrcPlaceToTransition jointpackage_petrinet2pnml_srcplacetotransition) {
        this.jointpackage_petrinet2pnml_srcplacetotransition = jointpackage_petrinet2pnml_srcplacetotransition;
    }
    public List<jointPackage_PetriNet2PNML_SrcTransitionToPlace> getJointpackage_petrinet2pnml_srctransitiontoplaces() {
        return jointpackage_petrinet2pnml_srctransitiontoplaces;
    }

    public void addJointpackage_petrinet2pnml_srctransitiontoplace(Jointpackage_petrinet2pnml_srctransitiontoplace jointpackage_petrinet2pnml_srctransitiontoplace) {
        this.jointpackage_petrinet2pnml_srctransitiontoplaces.add(jointpackage_petrinet2pnml_srctransitiontoplace);
    }
    public List<jointPackage_PetriNet2PNML_SrcPlaceToTransition> getJointpackage_petrinet2pnml_srcplacetotransitions() {
        return jointpackage_petrinet2pnml_srcplacetotransitions;
    }

    public void addJointpackage_petrinet2pnml_srcplacetotransition(Jointpackage_petrinet2pnml_srcplacetotransition jointpackage_petrinet2pnml_srcplacetotransition) {
        this.jointpackage_petrinet2pnml_srcplacetotransitions.add(jointpackage_petrinet2pnml_srcplacetotransition);
    }

}