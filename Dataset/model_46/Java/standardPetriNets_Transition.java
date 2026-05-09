





import java.util.List;
import java.util.ArrayList;

public class standardPetriNets_Transition  {

    private String name;





    private standardPetriNets_OutputArc standardpetrinets_outputarc;




    private standardPetriNets_PetriNet standardpetrinets_petrinet;


    public standardPetriNets_Transition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public standardPetriNets_OutputArc getStandardpetrinets_outputarc() {
        return standardpetrinets_outputarc;
    }

    public void setStandardpetrinets_outputarc(standardPetriNets_OutputArc standardpetrinets_outputarc) {
        this.standardpetrinets_outputarc = standardpetrinets_outputarc;
    }
    public standardPetriNets_PetriNet getStandardpetrinets_petrinet() {
        return standardpetrinets_petrinet;
    }

    public void setStandardpetrinets_petrinet(standardPetriNets_PetriNet standardpetrinets_petrinet) {
        this.standardpetrinets_petrinet = standardpetrinets_petrinet;
    }

}