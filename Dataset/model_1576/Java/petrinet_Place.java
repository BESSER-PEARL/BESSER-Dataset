





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place extends Node {

    private int nbJetons;



    public petrinet_Place(
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