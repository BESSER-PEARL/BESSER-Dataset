





import java.util.List;
import java.util.ArrayList;

public class petriNet_Noeud extends PetriNetElt {

    private String name;



    public petriNet_Noeud(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}