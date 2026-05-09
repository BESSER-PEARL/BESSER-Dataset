





import java.util.List;
import java.util.ArrayList;

public class petrinet_PetriNet extends RefPetriNets {

    private String name;



    public petrinet_PetriNet(
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