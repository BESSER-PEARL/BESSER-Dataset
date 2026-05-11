





import java.util.List;
import java.util.ArrayList;

public class tbase_TRoot  {






    private List<tbase_A> tbase_as;


    public tbase_TRoot(
    ) {
        this.tbase_as = new ArrayList<>();
    }

    public tbase_TRoot(
        ArrayList<tbase_A> tbase_as    ) {
        this.tbase_as = tbase_as;
    }


    public List<tbase_A> getTbase_as() {
        return tbase_as;
    }

    public void addTbase_a(Tbase_a tbase_a) {
        this.tbase_as.add(tbase_a);
    }

}