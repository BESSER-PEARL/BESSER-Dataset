





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Arc  {

    private int poids;
    private String arcType;



    public PetriNet_Arc(
        int poids,        String arcType    ) {
        this.poids = poids;
        this.arcType = arcType;
    }


    public int getPoids() {
        return poids;
    }

    public void setPoids(int poids) {
        this.poids = poids;
    }
    public String getArctype() {
        return arcType;
    }

    public void setArctype(String arcType) {
        this.arcType = arcType;
    }


}