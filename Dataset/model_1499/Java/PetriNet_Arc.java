





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Arc  {

    private String type;
    private String poids;



    public PetriNet_Arc(
        String type,        String poids    ) {
        this.type = type;
        this.poids = poids;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getPoids() {
        return poids;
    }

    public void setPoids(String poids) {
        this.poids = poids;
    }


}