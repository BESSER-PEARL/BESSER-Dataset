





import java.util.List;
import java.util.ArrayList;

public class ptn_Transition extends AbstractTransition {

    private int weight;



    public ptn_Transition(
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