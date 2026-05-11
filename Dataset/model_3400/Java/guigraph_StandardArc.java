





import java.util.List;
import java.util.ArrayList;

public class guigraph_StandardArc extends Arc {

    private int weight;



    public guigraph_StandardArc(
        int weight    ) {
        super(
        );
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }


}