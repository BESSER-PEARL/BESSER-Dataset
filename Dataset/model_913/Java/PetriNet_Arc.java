





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Arc extends PetriElement {

    private boolean isReadArc;
    private int poids;



    public PetriNet_Arc(
        boolean isReadArc,        int poids    ) {
        super(
        );
        this.isReadArc = isReadArc;
        this.poids = poids;
    }


    public boolean getIsreadarc() {
        return isReadArc;
    }

    public void setIsreadarc(boolean isReadArc) {
        this.isReadArc = isReadArc;
    }
    public int getPoids() {
        return poids;
    }

    public void setPoids(int poids) {
        this.poids = poids;
    }


}