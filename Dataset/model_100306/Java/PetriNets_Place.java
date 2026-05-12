





import java.util.List;
import java.util.ArrayList;

public class PetriNets_Place  {

    private String name;
    private int numberOfTokens;
    private int capacity;





    private PetriNets_OutputArc petrinets_outputarc;




    private PetriNets_InputArc petrinets_inputarc;


    public PetriNets_Place(
        String name,        int numberOfTokens,        int capacity    ) {
        this.name = name;
        this.numberOfTokens = numberOfTokens;
        this.capacity = capacity;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
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

    public PetriNets_OutputArc getPetrinets_outputarc() {
        return petrinets_outputarc;
    }

    public void setPetrinets_outputarc(PetriNets_OutputArc petrinets_outputarc) {
        this.petrinets_outputarc = petrinets_outputarc;
    }
    public PetriNets_InputArc getPetrinets_inputarc() {
        return petrinets_inputarc;
    }

    public void setPetrinets_inputarc(PetriNets_InputArc petrinets_inputarc) {
        this.petrinets_inputarc = petrinets_inputarc;
    }

}