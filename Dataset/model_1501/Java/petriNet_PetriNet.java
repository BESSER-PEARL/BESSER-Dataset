





import java.util.List;
import java.util.ArrayList;

public class petriNet_PetriNet  {

    private String name;





    private petriNet_PetriNetElt petrinet_petrinetelt;




    private List<petriNet_PetriNetElt> petrinet_petrinetelts;


    public petriNet_PetriNet(
        String name    ) {
        this.name = name;
        this.petrinet_petrinetelts = new ArrayList<>();
    }

    public petriNet_PetriNet(
        String name        ArrayList<petriNet_PetriNetElt> petrinet_petrinetelts    ) {
        this.name = name;
        this.petrinet_petrinetelts = petrinet_petrinetelts;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public petriNet_PetriNetElt getPetrinet_petrinetelt() {
        return petrinet_petrinetelt;
    }

    public void setPetrinet_petrinetelt(petriNet_PetriNetElt petrinet_petrinetelt) {
        this.petrinet_petrinetelt = petrinet_petrinetelt;
    }
    public List<petriNet_PetriNetElt> getPetrinet_petrinetelts() {
        return petrinet_petrinetelts;
    }

    public void addPetrinet_petrinetelt(Petrinet_petrinetelt petrinet_petrinetelt) {
        this.petrinet_petrinetelts.add(petrinet_petrinetelt);
    }

}