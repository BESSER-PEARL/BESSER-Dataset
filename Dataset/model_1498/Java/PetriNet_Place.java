





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Place extends PetriElement {

    private int nbJetons;



    public PetriNet_Place(
        int nbJetons    ) {
        super(
        );
        this.nbJetons = nbJetons;
    }


    public int getNbjetons() {
        return nbJetons;
    }

    public void setNbjetons(int nbJetons) {
        this.nbJetons = nbJetons;
    }


}