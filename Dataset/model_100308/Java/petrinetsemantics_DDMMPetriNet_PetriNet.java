





import java.util.List;
import java.util.ArrayList;

public class petrinetsemantics_DDMMPetriNet_PetriNet  {

    private String name;





    private List<Node> nodes;


    public petrinetsemantics_DDMMPetriNet_PetriNet(
        String name    ) {
        this.name = name;
        this.nodes = new ArrayList<>();
    }

    public petrinetsemantics_DDMMPetriNet_PetriNet(
        String name        ArrayList<Node> nodes    ) {
        this.name = name;
        this.nodes = nodes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Node> getNodes() {
        return nodes;
    }

    public void addNode(Node node) {
        this.nodes.add(node);
    }

}