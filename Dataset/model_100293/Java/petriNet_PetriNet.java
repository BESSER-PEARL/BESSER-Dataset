





import java.util.List;
import java.util.ArrayList;

public class petriNet_PetriNet  {

    private String name;





    private List<petriNet_OutputArc> petrinet_outputarcs;


    public petriNet_PetriNet(
        String name    ) {
        this.name = name;
        this.petrinet_outputarcs = new ArrayList<>();
    }

    public petriNet_PetriNet(
        String name        ArrayList<petriNet_OutputArc> petrinet_outputarcs    ) {
        this.name = name;
        this.petrinet_outputarcs = petrinet_outputarcs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<petriNet_OutputArc> getPetrinet_outputarcs() {
        return petrinet_outputarcs;
    }

    public void addPetrinet_outputarc(Petrinet_outputarc petrinet_outputarc) {
        this.petrinet_outputarcs.add(petrinet_outputarc);
    }

}