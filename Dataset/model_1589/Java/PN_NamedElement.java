





import java.util.List;
import java.util.ArrayList;

public class PN_NamedElement  {

    private String name;





    private PN_PetriNet pn_petrinet;


    public PN_NamedElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PN_PetriNet getPn_petrinet() {
        return pn_petrinet;
    }

    public void setPn_petrinet(PN_PetriNet pn_petrinet) {
        this.pn_petrinet = pn_petrinet;
    }

}