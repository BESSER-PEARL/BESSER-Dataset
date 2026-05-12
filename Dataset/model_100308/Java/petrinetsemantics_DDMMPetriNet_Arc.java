





import java.util.List;
import java.util.ArrayList;

public class petrinetsemantics_DDMMPetriNet_Arc  {

    private String kind;
    private int weight;





    private Node node;




    private Node node;




    private PetriNet petrinet;


    public petrinetsemantics_DDMMPetriNet_Arc(
        String kind,        int weight    ) {
        this.kind = kind;
        this.weight = weight;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public Node getNode() {
        return node;
    }

    public void setNode(Node node) {
        this.node = node;
    }
    public Node getNode() {
        return node;
    }

    public void setNode(Node node) {
        this.node = node;
    }
    public PetriNet getPetrinet() {
        return petrinet;
    }

    public void setPetrinet(PetriNet petrinet) {
        this.petrinet = petrinet;
    }

}