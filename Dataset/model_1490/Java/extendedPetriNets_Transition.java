





import java.util.List;
import java.util.ArrayList;

public class extendedPetriNets_Transition  {

    private String name;
    private String label;





    private extendedPetriNets_PetriNet extendedpetrinets_petrinet;


    public extendedPetriNets_Transition(
        String name,        String label    ) {
        this.name = name;
        this.label = label;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public extendedPetriNets_PetriNet getExtendedpetrinets_petrinet() {
        return extendedpetrinets_petrinet;
    }

    public void setExtendedpetrinets_petrinet(extendedPetriNets_PetriNet extendedpetrinets_petrinet) {
        this.extendedpetrinets_petrinet = extendedpetrinets_petrinet;
    }

}