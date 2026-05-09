





import java.util.List;
import java.util.ArrayList;

public class evoPetrinet_Arc extends Element {

    private String weight;



    public evoPetrinet_Arc(
        String weight    ) {
        super(
        );
        this.weight = weight;
    }


    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }


}