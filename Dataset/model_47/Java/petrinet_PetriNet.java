





import java.util.List;
import java.util.ArrayList;

public class petrinet_PetriNet  {

    private String name;





    private petrinet_System petrinet_system;


    public petrinet_PetriNet(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public petrinet_System getPetrinet_system() {
        return petrinet_system;
    }

    public void setPetrinet_system(petrinet_System petrinet_system) {
        this.petrinet_system = petrinet_system;
    }

}