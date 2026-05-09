





import java.util.List;
import java.util.ArrayList;

public class petrinet_Arc  {

    private String name;
    private int weight;





    private petrinet_Petrinet petrinet_petrinet;


    public petrinet_Arc(
        String name,        int weight    ) {
        this.name = name;
        this.weight = weight;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public petrinet_Petrinet getPetrinet_petrinet() {
        return petrinet_petrinet;
    }

    public void setPetrinet_petrinet(petrinet_Petrinet petrinet_petrinet) {
        this.petrinet_petrinet = petrinet_petrinet;
    }

}