





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Arc  {

    private String weight;
    private String name;



    public PetriNet_Arc(
        String weight,        String name    ) {
        this.weight = weight;
        this.name = name;
    }


    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}