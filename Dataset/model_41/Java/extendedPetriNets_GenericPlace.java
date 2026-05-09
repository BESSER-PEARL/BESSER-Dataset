





import java.util.List;
import java.util.ArrayList;

public class extendedPetriNets_GenericPlace  {

    private int capacity;
    private int numberOfTokens;
    private String name;





    private extendedPetriNets_OutputArc extendedpetrinets_outputarc;




    private extendedPetriNets_PetriNet extendedpetrinets_petrinet;


    public extendedPetriNets_GenericPlace(
        int capacity,        int numberOfTokens,        String name    ) {
        this.capacity = capacity;
        this.numberOfTokens = numberOfTokens;
        this.name = name;
    }


    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }
    public int getNumberoftokens() {
        return numberOfTokens;
    }

    public void setNumberoftokens(int numberOfTokens) {
        this.numberOfTokens = numberOfTokens;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public extendedPetriNets_OutputArc getExtendedpetrinets_outputarc() {
        return extendedpetrinets_outputarc;
    }

    public void setExtendedpetrinets_outputarc(extendedPetriNets_OutputArc extendedpetrinets_outputarc) {
        this.extendedpetrinets_outputarc = extendedpetrinets_outputarc;
    }
    public extendedPetriNets_PetriNet getExtendedpetrinets_petrinet() {
        return extendedpetrinets_petrinet;
    }

    public void setExtendedpetrinets_petrinet(extendedPetriNets_PetriNet extendedpetrinets_petrinet) {
        this.extendedpetrinets_petrinet = extendedpetrinets_petrinet;
    }

}