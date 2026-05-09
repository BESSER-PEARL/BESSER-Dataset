





import java.util.List;
import java.util.ArrayList;

public class extendedPetriNets_PetriNet  {

    private String name;





    private List<extendedPetriNets_OutputArc> extendedpetrinets_outputarcs;


    public extendedPetriNets_PetriNet(
        String name    ) {
        this.name = name;
        this.extendedpetrinets_outputarcs = new ArrayList<>();
    }

    public extendedPetriNets_PetriNet(
        String name        ArrayList<extendedPetriNets_OutputArc> extendedpetrinets_outputarcs    ) {
        this.name = name;
        this.extendedpetrinets_outputarcs = extendedpetrinets_outputarcs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<extendedPetriNets_OutputArc> getExtendedpetrinets_outputarcs() {
        return extendedpetrinets_outputarcs;
    }

    public void addExtendedpetrinets_outputarc(Extendedpetrinets_outputarc extendedpetrinets_outputarc) {
        this.extendedpetrinets_outputarcs.add(extendedpetrinets_outputarc);
    }

}