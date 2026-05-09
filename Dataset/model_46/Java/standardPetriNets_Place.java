





import java.util.List;
import java.util.ArrayList;

public class standardPetriNets_Place  {

    private int numOfTokens;
    private String name;
    private int capacity;





    private standardPetriNets_PetriNet standardpetrinets_petrinet;




    private standardPetriNets_OutputArc standardpetrinets_outputarc;


    public standardPetriNets_Place(
        int numOfTokens,        String name,        int capacity    ) {
        this.numOfTokens = numOfTokens;
        this.name = name;
        this.capacity = capacity;
    }


    public int getNumoftokens() {
        return numOfTokens;
    }

    public void setNumoftokens(int numOfTokens) {
        this.numOfTokens = numOfTokens;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }

    public standardPetriNets_PetriNet getStandardpetrinets_petrinet() {
        return standardpetrinets_petrinet;
    }

    public void setStandardpetrinets_petrinet(standardPetriNets_PetriNet standardpetrinets_petrinet) {
        this.standardpetrinets_petrinet = standardpetrinets_petrinet;
    }
    public standardPetriNets_OutputArc getStandardpetrinets_outputarc() {
        return standardpetrinets_outputarc;
    }

    public void setStandardpetrinets_outputarc(standardPetriNets_OutputArc standardpetrinets_outputarc) {
        this.standardpetrinets_outputarc = standardpetrinets_outputarc;
    }

}