





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place  {

    private String name;
    private int token;





    private petrinet_PetriNet petrinet_petrinet;


    public petrinet_Place(
        String name,        int token    ) {
        this.name = name;
        this.token = token;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getToken() {
        return token;
    }

    public void setToken(int token) {
        this.token = token;
    }

    public petrinet_PetriNet getPetrinet_petrinet() {
        return petrinet_petrinet;
    }

    public void setPetrinet_petrinet(petrinet_PetriNet petrinet_petrinet) {
        this.petrinet_petrinet = petrinet_petrinet;
    }

}