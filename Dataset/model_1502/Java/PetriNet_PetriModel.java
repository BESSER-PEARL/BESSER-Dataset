





import java.util.List;
import java.util.ArrayList;

public class PetriNet_PetriModel  {

    private String name;
    private String description;





    private List<PetriNet_PetriModel> petrinet_petrimodels;


    public PetriNet_PetriModel(
        String name,        String description    ) {
        this.name = name;
        this.description = description;
        this.petrinet_petrimodels = new ArrayList<>();
    }

    public PetriNet_PetriModel(
        String name,        String description        ArrayList<PetriNet_PetriModel> petrinet_petrimodels    ) {
        this.name = name;
        this.description = description;
        this.petrinet_petrimodels = petrinet_petrimodels;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<PetriNet_PetriModel> getPetrinet_petrimodels() {
        return petrinet_petrimodels;
    }

    public void addPetrinet_petrimodel(Petrinet_petrimodel petrinet_petrimodel) {
        this.petrinet_petrimodels.add(petrinet_petrimodel);
    }

}