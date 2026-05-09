





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Place extends Noeud {

    private int jeton;



    public PetriNet_Place(
        int jeton    ) {
        super(
        );
        this.jeton = jeton;
    }


    public int getJeton() {
        return jeton;
    }

    public void setJeton(int jeton) {
        this.jeton = jeton;
    }


}