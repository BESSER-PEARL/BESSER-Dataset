





import java.util.List;
import java.util.ArrayList;

public class standardPetriNets_PetriNet  {

    private String name;





    private List<standardPetriNets_OutputArc> standardpetrinets_outputarcs;


    public standardPetriNets_PetriNet(
        String name    ) {
        this.name = name;
        this.standardpetrinets_outputarcs = new ArrayList<>();
    }

    public standardPetriNets_PetriNet(
        String name        ArrayList<standardPetriNets_OutputArc> standardpetrinets_outputarcs    ) {
        this.name = name;
        this.standardpetrinets_outputarcs = standardpetrinets_outputarcs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<standardPetriNets_OutputArc> getStandardpetrinets_outputarcs() {
        return standardpetrinets_outputarcs;
    }

    public void addStandardpetrinets_outputarc(Standardpetrinets_outputarc standardpetrinets_outputarc) {
        this.standardpetrinets_outputarcs.add(standardpetrinets_outputarc);
    }

}