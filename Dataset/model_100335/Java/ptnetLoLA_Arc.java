





import java.util.List;
import java.util.ArrayList;

public class ptnetLoLA_Arc  {

    private int weight;





    private ptnetLoLA_PtNet ptnetlola_ptnet;


    public ptnetLoLA_Arc(
        int weight    ) {
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public ptnetLoLA_PtNet getPtnetlola_ptnet() {
        return ptnetlola_ptnet;
    }

    public void setPtnetlola_ptnet(ptnetLoLA_PtNet ptnetlola_ptnet) {
        this.ptnetlola_ptnet = ptnetlola_ptnet;
    }

}