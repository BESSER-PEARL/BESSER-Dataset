





import java.util.List;
import java.util.ArrayList;

public class R  {






    private List<Abis> abiss;


    public R(
    ) {
        this.abiss = new ArrayList<>();
    }

    public R(
        ArrayList<Abis> abiss    ) {
        this.abiss = abiss;
    }


    public List<Abis> getAbiss() {
        return abiss;
    }

    public void addAbis(Abis abis) {
        this.abiss.add(abis);
    }

}