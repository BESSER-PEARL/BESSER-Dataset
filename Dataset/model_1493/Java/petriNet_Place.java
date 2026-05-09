





import java.util.List;
import java.util.ArrayList;

public class petriNet_Place extends PetriElement {

    private int nbJetons;



    public petriNet_Place(
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