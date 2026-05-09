





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place  {

    private String name;





    private petrinet_Petrinet petrinet_petrinet;


    public petrinet_Place(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public petrinet_Petrinet getPetrinet_petrinet() {
        return petrinet_petrinet;
    }

    public void setPetrinet_petrinet(petrinet_Petrinet petrinet_petrinet) {
        this.petrinet_petrinet = petrinet_petrinet;
    }

}