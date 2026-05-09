





import java.util.List;
import java.util.ArrayList;

public class extendedPetriNets_GenericPlace  {

    private int numberOfTokens;
    private int capacity;
    private String name;





    private extendedPetriNets_PetriNet extendedpetrinets_petrinet;


    public extendedPetriNets_GenericPlace(
        int numberOfTokens,        int capacity,        String name    ) {
        this.numberOfTokens = numberOfTokens;
        this.capacity = capacity;
        this.name = name;
    }


    public int getNumberoftokens() {
        return numberOfTokens;
    }

    public void setNumberoftokens(int numberOfTokens) {
        this.numberOfTokens = numberOfTokens;
    }
    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public extendedPetriNets_PetriNet getExtendedpetrinets_petrinet() {
        return extendedpetrinets_petrinet;
    }

    public void setExtendedpetrinets_petrinet(extendedPetriNets_PetriNet extendedpetrinets_petrinet) {
        this.extendedpetrinets_petrinet = extendedpetrinets_petrinet;
    }

}