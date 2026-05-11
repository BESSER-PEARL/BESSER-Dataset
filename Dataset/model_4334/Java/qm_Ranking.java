





import java.util.List;
import java.util.ArrayList;

public class qm_Ranking  {

    private float weight;
    private int rank;



    public qm_Ranking(
        float weight,        int rank    ) {
        this.weight = weight;
        this.rank = rank;
    }


    public float getWeight() {
        return weight;
    }

    public void setWeight(float weight) {
        this.weight = weight;
    }
    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }


}