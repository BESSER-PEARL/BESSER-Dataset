





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Arc  {

    private String name;
    private String weight;



    public PetriNet_Arc(
        String name,        String weight    ) {
        this.name = name;
        this.weight = weight;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }


}