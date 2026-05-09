





import java.util.List;
import java.util.ArrayList;

public class highlevelnets_tokentypes_TokenTypeElementNet extends TokenType {






    private HighLevelPetriNet highlevelpetrinet;




    private List<ElementNetMarked> elementnetmarkeds;


    public highlevelnets_tokentypes_TokenTypeElementNet(
    ) {
        super(
        );
        this.elementnetmarkeds = new ArrayList<>();
    }

    public highlevelnets_tokentypes_TokenTypeElementNet(
        ArrayList<ElementNetMarked> elementnetmarkeds    ) {
        this.elementnetmarkeds = elementnetmarkeds;
    }


    public HighLevelPetriNet getHighlevelpetrinet() {
        return highlevelpetrinet;
    }

    public void setHighlevelpetrinet(HighLevelPetriNet highlevelpetrinet) {
        this.highlevelpetrinet = highlevelpetrinet;
    }
    public List<ElementNetMarked> getElementnetmarkeds() {
        return elementnetmarkeds;
    }

    public void addElementnetmarked(Elementnetmarked elementnetmarked) {
        this.elementnetmarkeds.add(elementnetmarked);
    }

}